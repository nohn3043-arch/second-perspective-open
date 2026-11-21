#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Second Perspective Gate — AI Verify test-plugin algorithm component.

Interface draft aligned with the official v2 plugin contract
(aiverify-developer-tools / aiverify-algorithm-template):

* ``Plugin.generate()`` is the core-logic entry point; results land in
  ``self._results`` and must match ``output.schema.json``.
* Custom arguments come from ``input.schema.json`` via ``algo_init.py``
  (``input_arguments``) and the CLI parser in ``plugin_init.py``.

Gate mapping (fail-closed):

    AUDIT_PASS -> RELEASE    AUDIT_WARN -> HOLD    AUDIT_HALT -> BLOCK
    missing / malformed report -> BLOCK (fail-closed)

Modes
-----
post-hoc (shipped here): verifies an engine-produced credential view and
    extracts the gate decision. Engine-free, stdlib-only, offline, deterministic.
inline (licensed delivery): with the private SPE engine available the operator
    runs it pre-release and feeds its report here; the mapping is identical.

Zero third-party dependencies · deterministic (identical input -> identical
output, byte-stable ``gate_digest``).
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Dict, Optional

__all__ = [
    "LEVEL_TO_GATE",
    "SecondPerspectiveGateAlgo",
    "extract_level",
    "run",
]

LEVEL_TO_GATE = {
    "AUDIT_PASS": "RELEASE",
    "AUDIT_WARN": "HOLD",
    "AUDIT_HALT": "BLOCK",
}

_FAIL_CLOSED_REASON = "fail-closed: ACC verdict level missing or malformed"


def _canonical(obj: Any) -> bytes:
    """Stable serialization for digesting (bilingual-safe, key-sorted)."""
    return json.dumps(obj, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def extract_level(report: Dict[str, Any]) -> Optional[str]:
    """Return the ACC verdict level from an SPE credential-view report, or None."""
    try:
        level = report["analysis"]["ACC"]["verdict"]["level"]
    except (KeyError, TypeError):
        return None
    return level if isinstance(level, str) else None


def run(report: Dict[str, Any],
        input_arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Produce the gate verdict record for one SPE credential-view report.

    Arguments (from ``input.schema.json`` via ``algo_init.py``):
        require_anchor — when true, anything but an ANCHORED responsibility
                         anchor forces BLOCK even on a passing verification.
    """
    args = dict(input_arguments or {})
    require_anchor = bool(args.get("require_anchor", False))

    lineage = report.get("lineage", {}) if isinstance(report, dict) else {}
    acc = report.get("analysis", {}).get("ACC", {}) if isinstance(report, dict) else {}
    verdict = acc.get("verdict", {}) if isinstance(acc, dict) else {}
    certificate = acc.get("certificate", {}) if isinstance(acc, dict) else {}
    responsibility = acc.get("responsibility", {}) if isinstance(acc, dict) else {}

    level = extract_level(report)
    if level is None:
        gate, reason = "BLOCK", _FAIL_CLOSED_REASON
    else:
        gate, reason = LEVEL_TO_GATE.get(level, "BLOCK"), "mapped from ACC verdict level"

    anchor_status = responsibility.get("anchor_status")
    if gate != "BLOCK" and require_anchor and anchor_status != "ANCHORED":
        gate = "BLOCK"
        reason = "require_anchor: responsibility anchor is not ANCHORED"

    payload: Dict[str, Any] = {
        "gate": gate,
        "reason": reason,
        "level": level,
        "halt_count": verdict.get("halt_count"),
        "warn_items": verdict.get("warn_items", []),
        "summary": verdict.get("summary"),
        "spe_version": lineage.get("spe_version"),
        "grammar_version": lineage.get("grammar_version"),
        "anchor_status": anchor_status,
        "input_digest": certificate.get("input_digest"),
        "certificate_present": bool(certificate.get("signature"))
        and bool(certificate.get("input_digest")),
        "require_anchor": require_anchor,
    }
    payload["gate_digest"] = hashlib.sha256(_canonical(payload)).hexdigest()
    return payload


class SecondPerspectiveGateAlgo:
    """Plugin class following the official v2 algorithm-template contract.

    The official base class is imported when the AI Verify test engine is
    installed (v2.x alpha: ``pip install aiverify-test-engine==2.0.0a1``);
    without it the class degrades to a plain object so the post-hoc mode still
    runs standalone under stdlib-only environments.
    """

    try:  # official host present -> inherit its plugin contract
        from aiverify_test_engine.plugin import AbstractAlgo  # type: ignore
    except Exception:  # standalone mode (stdlib only)
        AbstractAlgo = object  # type: ignore[misc,assignment]

    def __init__(self) -> None:
        self.meta = {
            "name": "second_perspective_gate",
            "description": "Deterministic gate over SPE verification verdicts "
                           "(RELEASE / HOLD / BLOCK, fail-closed)",
            "version": "0.1.0",
        }
        # official v2 host-injected attributes
        self._data_instance = None
        self._model_instance = None
        self._ground_truth_instance = None
        self._progress_inst = None
        self._results: Optional[Dict[str, Any]] = None

    def setup(self, data_instance: Any = None, model_instance: Any = None,
              ground_truth_instance: Any = None, progress_inst: Any = None) -> None:
        """Receive host-injected instances (official v2 template pattern)."""
        self._data_instance = data_instance
        self._model_instance = model_instance
        self._ground_truth_instance = ground_truth_instance
        self._progress_inst = progress_inst

    def generate(self) -> None:
        """Core logic per the official template: fill ``self._results``.

        The gate is model-agnostic: it verifies an SPE credential-view report
        (delivered via ``self._data_instance``), not model predictions.
        """
        data = self._data_instance
        report = data.get_data() if hasattr(data, "get_data") else data
        self._results = run(report)

    def execute(self, input_data: Dict[str, Any],
                input_arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Standalone entry point (no host required)."""
        return run(input_data, input_arguments)
