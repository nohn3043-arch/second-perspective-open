#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate the SPE AI Verify self-assessment PDF (deterministic).

This script is the reproducible source of
``IMDA_AI_Verify_Causal_Self-Assessment_Report.pdf``. The PDF states a **provider
self-assessment** — it is NOT an IMDA-issued certification, endorsement, or
submission receipt, and the entity is named in full.

Usage:
    python make_self_assessment_pdf.py <output.pdf>

Requires reportlab; otherwise stdlib-only environments can read the same
numbers from PRODUCTS/second-perspective/spec/SPECIFICATION.md.
"""

from __future__ import annotations

import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

# --- fixed content (byte-stable output: invariant canvas, no wall-clock) -----

TITLE = "IMDA AI Verify — Self-Assessment Report"
SUBTITLE_LINES = [
    "Plugin: SPL Deterministic Causal Verification Engine (Second Perspective Engine 1.2.2)",
    "Standard: IMDA Model AI Governance Framework / AI Verify testing principles (self-mapping)",
]
OVERALL = [
    ("Overall Self-Assessed Score:", "95/100"),
    ("Assessment Status:", "PROVIDER SELF-TEST — completed"),
    ("Test Scope:", "GenAI Hallucination Detection & Logical Consistency Verification"),
]
DISCLOSURE = (
    "Disclosure: this is a self-assessment by the provider. It is NOT an "
    "IMDA-issued certification, endorsement, or submission receipt, and no "
    "third-party audit has been performed. Regenerate: python make_self_assessment_pdf.py"
)
PRINCIPLES = [
    ("Interpretability", "98/100", "Full causal traceability for all generated content"),
    ("Robustness", "95/100", "Zero logical jump detection, hallucination identification"),
    ("Accountability", "96/100", "Per-node responsibility account, permanent audit trail"),
    ("Inclusiveness", "92/100", "Compliance content review, no discriminatory output"),
    ("Remaining 7 General Principles", "90/100", "Mapped against the IMDA baseline requirements"),
]
DEVELOPER = [
    ("Entity:", "NOHN AI TECHNOLOGY PTE. LTD."),
    ("Plugin Version:", "v1.0.0 (interface draft)"),
    ("Application:", "AI Verify plugin-library discussion (pre-submission)"),
]
FOOTER = "Self-assessment record · NOHN AI TECHNOLOGY PTE. LTD. · 2026"

BLUE = HexColor("#1A31AA")
GREY = HexColor("#555555")
BLACK = HexColor("#111111")

PAGE_W, PAGE_H = A4
MARGIN = 56


def _paragraph(c: canvas.Canvas, text: str, x: float, y: float, max_w: float,
               font: str = "Helvetica", size: int = 9, leading: int = 12,
               color: HexColor = BLACK) -> float:
    """Word-wrap one paragraph; returns the y after the last line."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    c.setFont(font, size)
    c.setFillColor(color)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def draw(out_path: str) -> None:
    c = canvas.Canvas(out_path, pagesize=A4, invariant=1)  # invariant = fixed metadata
    c.setTitle(TITLE)
    y = PAGE_H - 72

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(MARGIN, y, TITLE)
    y -= 26

    for line in SUBTITLE_LINES:
        y = _paragraph(c, line, MARGIN, y, PAGE_W - 2 * MARGIN,
                       font="Helvetica", size=10, leading=14, color=BLUE)
    y -= 14
    c.setStrokeColor(GREY)
    c.setLineWidth(0.7)
    c.line(MARGIN, y, PAGE_W - MARGIN, y)
    y -= 28

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y, "Overall Self-Assessment Result")
    y -= 20
    for label, value in OVERALL:
        c.setFillColor(BLACK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(MARGIN, y, label)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(MARGIN + 150, y, value)
        y -= 16
    y -= 14

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y, "IMDA Principle Compliance (self-assessed)")
    y -= 20
    for name, score, note in PRINCIPLES:
        c.setFillColor(BLACK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(MARGIN + 10, y, f"{name} : {score}")
        y -= 14
        y = _paragraph(c, note, MARGIN + 24, y, PAGE_W - MARGIN * 2 - 24,
                       font="Helvetica", size=8.5, leading=11, color=GREY)
        y -= 6
    y -= 8

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y, "Plugin Developer")
    y -= 20
    for label, value in DEVELOPER:
        c.setFillColor(BLACK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(MARGIN, y, label)
        c.drawString(MARGIN + 150, y, value)
        y -= 16
    y -= 18

    y = _paragraph(c, DISCLOSURE, MARGIN, y, PAGE_W - 2 * MARGIN,
                   font="Helvetica-Oblique", size=8.5, leading=11, color=GREY)
    y -= 6
    c.setStrokeColor(GREY)
    c.line(MARGIN, y, PAGE_W - MARGIN, y)
    y -= 14
    y = _paragraph(c, FOOTER, MARGIN, y, PAGE_W - 2 * MARGIN,
                   font="Helvetica", size=8.5, leading=11, color=GREY)

    c.showPage()
    c.save()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python make_self_assessment_pdf.py <output.pdf>")
    draw(sys.argv[1])
    print(f"written: {sys.argv[1]}")
