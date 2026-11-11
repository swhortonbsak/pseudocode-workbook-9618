#!/usr/bin/env python3
"""Check pagination, searchable content, marking totals and text boundaries."""
import hashlib
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
pdf = ROOT / "Pseudocode-Workbook-9618.pdf"
data = json.loads((ROOT / "workbook.json").read_text())
doc = pymupdf.open(pdf)
assert len(doc) == 34, f"Expected 34 pages, got {len(doc)}"
assert len(doc.get_toc()) == 34, "Missing PDF navigation entries"

all_text = "\n".join(page.get_text() for page in doc)
assert "\ufffd" not in all_text, "Missing or invalid character encoding"
assert "←" in all_text, "Assignment arrows are missing"

for i, page in enumerate(doc):
    text = page.get_text()
    assert f"{i + 1:02d} / 34" in text, f"Wrong footer on page {i + 1}"
    assert len(text.strip()) > 250, f"Unexpected near-empty page {i + 1}"
    for block in page.get_text("dict")["blocks"]:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                x0, y0, x1, y1 = span["bbox"]
                assert x0 >= 35 and x1 <= page.rect.width - 35, (i + 1, span["text"])
                assert y0 >= 12 and y1 <= page.rect.height - 12, (i + 1, span["text"])
                # Main content must remain above the footer rule.
                if y0 > 50:
                    assert y1 < page.rect.height - 47 or y0 > page.rect.height - 40, (i + 1, span["text"])

for task in data["tasks"] + data["advanced"]:
    assert sum(mark for _, mark in task["rubric"]) == task["marks"], task["id"]
    # Verify that the whole solution was typeset on its intended page.
    number = task["id"] + 12 if task["id"] <= 12 else task["id"] + 16
    compact_page = "".join(doc[number - 1].get_text().split())
    for line in task["code"].splitlines():
        assert "".join(line.split()) in compact_page, (task["id"], line)

report = {
    "file": pdf.name,
    "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "pages": len(doc),
    "core_tasks": len(data["tasks"]),
    "advanced_tasks": len(data["advanced"]),
    "suggested_marks": sum(t["marks"] for t in data["tasks"] + data["advanced"]),
    "checks": {
        "expected_pagination": "passed",
        "pdf_navigation": "passed",
        "page_footers": "passed",
        "searchable_text_and_assignment_arrows": "passed",
        "text_within_page_and_above_footer": "passed",
        "complete_solution_code_on_expected_pages": "passed",
        "mark_allocations": "passed",
    },
    "review_notes": [
        "Rendered contact sheets for all 34 pages were visually inspected.",
        "Worked solutions and listed boundary cases were manually reviewed; automated checks here cover the PDF and marking totals, not pseudocode execution.",
    ],
}
(ROOT / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
