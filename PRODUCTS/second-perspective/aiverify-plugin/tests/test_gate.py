#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Second Perspective Gate — plugin tests (stdlib unittest, offline).

Run:  python -m unittest discover -s tests -v     (from aiverify-plugin/)
"""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from second_perspective_gate.algo import run  # noqa: E402

DATA = Path(__file__).resolve().parents[1] / "data"


def load(name: str):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)


class TestGateDeterminism(unittest.TestCase):
    def test_identical_input_identical_output(self):
        report = load("sample_report.json")
        first, second = run(report), run(report)
        self.assertEqual(first, second)
        self.assertEqual(first["gate_digest"], second["gate_digest"])

    def test_gate_digest_is_verifiable(self):
        report = load("sample_report.json")
        out = run(report)
        payload = {k: v for k, v in out.items() if k != "gate_digest"}
        expected = hashlib.sha256(
            json.dumps(payload, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":")).encode("utf-8")).hexdigest()
        self.assertEqual(out["gate_digest"], expected)


class TestGateMapping(unittest.TestCase):
    def test_audit_warn_maps_to_hold(self):
        out = run(load("sample_report.json"))
        self.assertEqual(out["level"], "AUDIT_WARN")
        self.assertEqual(out["gate"], "HOLD")
        self.assertEqual(out["spe_version"], "1.2.2")
        self.assertTrue(out["certificate_present"])

    def test_audit_pass_maps_to_release(self):
        report = load("sample_report.json")
        report["analysis"]["ACC"]["verdict"]["level"] = "AUDIT_PASS"
        self.assertEqual(run(report)["gate"], "RELEASE")

    def test_audit_halt_maps_to_block(self):
        report = load("sample_report.json")
        report["analysis"]["ACC"]["verdict"]["level"] = "AUDIT_HALT"
        self.assertEqual(run(report)["gate"], "BLOCK")

    def test_malformed_report_fails_closed(self):
        self.assertEqual(run({})["gate"], "BLOCK")
        self.assertEqual(run({"analysis": {}})["gate"], "BLOCK")
        self.assertIn("fail-closed", run({})["reason"])

    def test_unknown_level_fails_closed(self):
        report = load("sample_report.json")
        report["analysis"]["ACC"]["verdict"]["level"] = "SOMETHING_ELSE"
        self.assertEqual(run(report)["gate"], "BLOCK")

    def test_require_anchor_argument_forces_block(self):
        report = load("sample_report.json")
        report["analysis"]["ACC"]["verdict"]["level"] = "AUDIT_PASS"
        report["analysis"]["ACC"].setdefault("responsibility", {})["anchor_status"] = "UNANCHORED"
        self.assertEqual(run(report)["gate"], "RELEASE")           # default: no anchor requirement
        forced = run(report, {"require_anchor": True})
        self.assertEqual(forced["gate"], "BLOCK")
        self.assertIn("require_anchor", forced["reason"])


class TestGateTamperSensitivity(unittest.TestCase):
    def test_tamper_changes_digest(self):
        report = load("sample_report.json")
        baseline = run(report)["gate_digest"]
        report["analysis"]["ACC"]["verdict"]["halt_count"] = 1
        self.assertNotEqual(run(report)["gate_digest"], baseline)


if __name__ == "__main__":
    unittest.main(verbosity=2)
