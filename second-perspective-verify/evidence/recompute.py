#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Engine-free recompute of a frozen Second-Perspective audit chain.

Zero dependencies. Python 3 standard library only. No engine, no licence, no network.

    python recompute.py            # recompute the chain, compare against expected.json
    python recompute.py --tamper   # edit one byte on a temp copy and show it is detected
    python recompute.py --json     # machine-readable result

What this proves
    The frozen chain is internally consistent — every link matches its predecessor and
    every event's content still hashes to the value that was sealed at append time —
    and the resulting root equals the root published in expected.json.

What this does NOT prove
    That the chain binds to any particular decision input. The chain covers the derived
    audit report, not the raw input. See README.md in this folder (disclosed limitation V3b).

Exit code: 0 = reproduced and intact; 1 = mismatch, tamper, or malformed chain.
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
EXPECTED = os.path.join(HERE, "expected.json")

START_SENTINEL = "ROOT"


def event_hash(event):
    """Reproduce the engine's chain hash for one event.

    Only these five fields are hashed. `index` and `sealed_hash` are outside the body.
    """
    blob = json.dumps({
        "event_type": event["event_type"],
        "payload": event["payload"],
        "prev_hash": event["prev_hash"],
        "timestamp": event["timestamp"],
        "nonce": event["nonce"],
    }, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def recompute(path):
    """Walk the chain and return (event_count, root). Raises ChainError on any break."""
    prev = START_SENTINEL
    last = START_SENTINEL
    n = 0
    with io.open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ev = json.loads(line)
            if ev.get("index") != n:
                raise ChainError("index gap at %d (found %r)" % (n, ev.get("index")))
            if ev.get("prev_hash") != prev:
                raise ChainError("link broken at %d" % n)
            if not ev.get("sealed_hash"):
                raise ChainError("event %d was never sealed" % n)
            h = event_hash(ev)
            if h != ev["sealed_hash"]:
                raise ChainError("content tampered at %d" % n)
            prev = h
            last = h
            n += 1
    return n, last


class ChainError(Exception):
    pass


def run_tamper(path):
    """Mutate one byte of a copy and prove the recomputation rejects it."""
    tmpdir = tempfile.mkdtemp(prefix="spe-evidence-")
    dest = os.path.join(tmpdir, "audit_chain.jsonl")
    try:
        shutil.copyfile(path, dest)
        with io.open(dest, encoding="utf-8") as f:
            events = [json.loads(l) for l in f if l.strip()]
        if not events:
            return "no events to tamper with"
        # Change the content the seal is meant to protect. One inserted key is enough:
        # the JSON stays valid, so this reaches the hash comparison instead of failing
        # to parse — which is what a real tamper would look like.
        payload = events[0]["payload"]
        if not isinstance(payload, dict):
            return "event 0 payload is not an object"
        payload["_tamper_demo"] = 1
        with io.open(dest, "w", encoding="utf-8", newline="\n") as f:
            for ev in events:
                f.write(json.dumps(ev, ensure_ascii=False, sort_keys=True) + "\n")
        try:
            recompute(dest)
        except (ChainError, ValueError) as exc:
            return "detected: %s" % exc
        return "NOT DETECTED — this would be a defect"
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Engine-free audit-chain recomputation")
    ap.add_argument("--tamper", action="store_true",
                    help="also demonstrate that a one-byte edit is detected")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    with io.open(EXPECTED, encoding="utf-8") as f:
        expected = json.load(f)

    result = {"chain": CHAIN, "expected_root": expected.get("chain_root_hash")}

    try:
        n, root = recompute(CHAIN)
    except (ChainError, ValueError) as exc:
        result.update({"status": "FAIL", "reason": str(exc)})
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.json
              else "FAIL: %s" % exc)
        return 1

    result.update({
        "event_count": n,
        "expected_event_count": expected.get("event_count"),
        "computed_root": root,
        "root_matches": root == expected.get("chain_root_hash"),
        "event_count_matches": n == expected.get("event_count"),
    })

    if args.tamper:
        result["tamper_check"] = run_tamper(CHAIN)

    ok = result["root_matches"] and result["event_count_matches"]
    if args.tamper:
        ok = ok and result["tamper_check"].startswith("detected")
    result["status"] = "PASS" if ok else "FAIL"

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print("events          : %d (expected %s)" % (n, expected.get("event_count")))
        print("computed root   : %s" % root)
        print("expected root   : %s" % expected.get("chain_root_hash"))
        print("root matches    : %s" % result["root_matches"])
        if args.tamper:
            print("tamper check    : %s" % result["tamper_check"])
        print("result          : %s" % result["status"])
        print()
        print("Scope: this verifies the frozen chain is intact and reproducible by")
        print("third-party code. It does NOT bind the chain to the original decision")
        print("input (disclosed limitation V3b). See README.md in this folder.")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
