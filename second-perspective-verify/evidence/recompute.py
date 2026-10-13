#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Engine-free verification of a frozen Second-Perspective evidence package.

Zero dependencies. Python 3 standard library only. No engine, no licence, no network.

    python recompute.py            # run all checks against expected.json
    python recompute.py --tamper   # + show that edits to the input, the report, and
                                   #   the chain are each detected
    python recompute.py --json     # machine-readable result

Checks, in order — each one is an independent link in the chain of custody:

    C1  chain integrity   every event hashes to the value sealed at append time,
                          and every link points at its predecessor
    C2  chain root        the last sealed hash equals the published root
    C3  input binding     sha256(decision_input.json) == expected.input_digest
    C4  input in report   the published report view carries that same input digest
    C5  report binding    sha256(report_credential_view.json)[:16] == expected.report_hash
    C6  report on chain   the chain event payload carries that same report_hash

What this proves
    The published input, the published report view and the published chain are bound
    to each other and to the published root, and every one of those links is
    recomputable by third-party code using the standard library alone.

What this does NOT prove
    That the report was produced honestly from the input, or that the engine is
    correct. It verifies the record, not the reasoning. See README.md in this folder.

Exit code: 0 = all checks pass; 1 = any check fails.
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN = os.path.join(HERE, "audit_chain.jsonl")
INPUT = os.path.join(HERE, "decision_input.json")
REPORT = os.path.join(HERE, "report_credential_view.json")
EXPECTED = os.path.join(HERE, "expected.json")

START_SENTINEL = "ROOT"


class CheckFailed(Exception):
    pass


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def event_hash(event):
    """Reproduce the engine's chain hash. Only these five fields are hashed."""
    blob = json.dumps({
        "event_type": event["event_type"],
        "payload": event["payload"],
        "prev_hash": event["prev_hash"],
        "timestamp": event["timestamp"],
        "nonce": event["nonce"],
    }, sort_keys=True, ensure_ascii=False, default=str)
    return sha256_bytes(blob.encode("utf-8"))


def walk_chain(path):
    """C1/C2: return (event_count, root, first_payload). Raises on any break."""
    prev = START_SENTINEL
    last = START_SENTINEL
    first_payload = None
    n = 0
    with io.open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ev = json.loads(line)
            if ev.get("index") != n:
                raise CheckFailed("C1 index gap at %d" % n)
            if ev.get("prev_hash") != prev:
                raise CheckFailed("C1 link broken at %d" % n)
            if not ev.get("sealed_hash"):
                raise CheckFailed("C1 event %d was never sealed" % n)
            h = event_hash(ev)
            if h != ev["sealed_hash"]:
                raise CheckFailed("C1 content tampered at %d" % n)
            if first_payload is None:
                first_payload = ev.get("payload") or {}
            prev = h
            last = h
            n += 1
    return n, last, first_payload


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def run_checks(tmpdir=None):
    """Run C1–C6 against the given root path (default: this folder)."""
    d = tmpdir or HERE
    chain = os.path.join(d, "audit_chain.jsonl")
    inp = os.path.join(d, "decision_input.json")
    rep = os.path.join(d, "report_credential_view.json")
    with io.open(os.path.join(d, "expected.json"), encoding="utf-8") as f:
        expected = json.load(f)

    out = {}

    n, root, payload = walk_chain(chain)
    out["C1_chain_integrity"] = "pass"
    out["C2_chain_root"] = "pass" if root == expected["chain_root_hash"] else (
        "FAIL: %s != %s" % (root, expected["chain_root_hash"]))

    digest = sha256_bytes(read_bytes(inp))
    out["C3_input_binding"] = "pass" if digest == expected["input_digest"] else (
        "FAIL: %s != %s" % (digest, expected["input_digest"]))

    with io.open(rep, encoding="utf-8") as f:
        view = json.load(f)
    embedded = (((view.get("analysis") or {}).get("ACC") or {})
                .get("certificate") or {}).get("input_digest")
    out["C4_input_in_report"] = "pass" if embedded == expected["input_digest"] else (
        "FAIL: report view carries %r" % embedded)

    rhash = sha256_bytes(read_bytes(rep))[:16]
    out["C5_report_binding"] = "pass" if rhash == expected["report_hash"] else (
        "FAIL: %s != %s" % (rhash, expected["report_hash"]))

    out["C6_report_on_chain"] = "pass" if payload.get("report_hash") == expected["report_hash"] else (
        "FAIL: chain carries %r" % payload.get("report_hash"))

    out["event_count"] = n
    out["chain_root_hash"] = root
    out["input_digest"] = digest
    out["report_hash"] = rhash
    return out


def tamper_report():
    """Edit each of the three artifacts in turn and report what gets caught."""
    rows = []
    def append_byte(target):
        with open(target, "ab") as f:
            f.write(b" ")

    def mutate_event(target):
        # The chain's hash covers event content, not file bytes, so appending whitespace
        # is not a tamper. Change the content instead — that is what C1 guards.
        with io.open(target, encoding="utf-8") as f:
            events = [json.loads(l) for l in f if l.strip()]
        if not events:
            return
        payload = events[0].get("payload")
        if isinstance(payload, dict):
            payload["_tamper_demo"] = 1
        with io.open(target, "w", encoding="utf-8", newline="\n") as f:
            for ev in events:
                f.write(json.dumps(ev, ensure_ascii=False, sort_keys=True) + "\n")

    for label, filename, mutate in (
        ("input file", "decision_input.json", append_byte),
        ("report view", "report_credential_view.json", append_byte),
        ("chain file", "audit_chain.jsonl", mutate_event),
    ):
        tmpdir = tempfile.mkdtemp(prefix="spe-evidence-")
        try:
            for name in ("audit_chain.jsonl", "decision_input.json",
                         "report_credential_view.json", "expected.json"):
                shutil.copyfile(os.path.join(HERE, name), os.path.join(tmpdir, name))
            mutate(os.path.join(tmpdir, filename))
            try:
                res = run_checks(tmpdir)
                failed = [k for k in res if k.startswith("C") and not str(res[k]).startswith("pass")]
                rows.append((label, "detected: " + ", ".join(failed) if failed
                             else "NOT DETECTED - this would be a defect"))
            except CheckFailed as exc:
                rows.append((label, "detected: %s" % exc))
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description="Engine-free evidence verification")
    ap.add_argument("--tamper", action="store_true",
                    help="also show that edits to each artifact are detected")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    if not os.path.exists(EXPECTED):
        print("missing expected.json next to recompute.py")
        return 1

    try:
        res = run_checks()
    except CheckFailed as exc:
        print("FAIL: %s" % exc)
        return 1
    except ValueError as exc:
        print("FAIL: malformed chain (%s)" % exc)
        return 1

    tamper = tamper_report() if args.tamper else None
    ok = all(str(v).startswith("pass") for k, v in res.items() if k.startswith("C"))
    if tamper is not None:
        ok = ok and all(t[1].startswith("detected") for t in tamper)

    if args.json:
        res["tamper"] = tamper
        res["status"] = "PASS" if ok else "FAIL"
        print(json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print("events          : %d (expected %s)" % (res["event_count"],
              json.load(io.open(EXPECTED, encoding='utf-8'))["event_count"]))
        print("chain root      : %s" % res["chain_root_hash"])
        print("input digest    : %s" % res["input_digest"])
        print("report hash     : %s" % res["report_hash"])
        print()
        for k in sorted(k for k in res if k.startswith("C")):
            print("  %-22s %s" % (k, res[k]))
        if tamper is not None:
            print()
            for label, verdict in tamper:
                print("  tamper %-12s %s" % (label, verdict))
        print()
        print("result          : %s" % ("PASS" if ok else "FAIL"))
        print()
        print("Scope: this binds the published input, report view and chain to each other")
        print("and to the published root. It verifies the record, not the reasoning —")
        print("it does not show that the report was derived honestly from the input.")
        print("See README.md in this folder.")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
