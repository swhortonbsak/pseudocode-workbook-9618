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
layout = json.loads((ROOT / "page-layout.json").read_text())
assert len(doc) == len(layout) == 56, f"Expected 56 pages, got {len(doc)}"
assert len(doc.get_toc()) == len(layout), "Missing PDF navigation entries"

all_text = "\n".join(page.get_text() for page in doc)
assert "\ufffd" not in all_text, "Missing or invalid character encoding"
assert "←" in all_text, "Assignment arrows are missing"

for i, page in enumerate(doc):
    text = page.get_text()
    assert f"{i + 1:02d} / {len(layout)}" in text, f"Wrong footer on page {i + 1}"
    assert len(text.strip()) > 200, f"Unexpected near-empty page {i + 1}"
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

solutions = [entry for entry in layout if entry["role"] == "solution"]
questions = [entry for entry in layout if entry["role"] == "question"]
responses = [entry for entry in layout if entry["role"] == "response"]
assert len(questions) == len(responses) == len(solutions) == 16
assert [entry["task_id"] for entry in solutions] == list(range(1, 17))
first_solution_page = solutions[0]["page"]
assert first_solution_page == 41
assert all(entry["role"] == "solution" for entry in layout[first_solution_page - 1:]), "Mark schemes must be the final section"
for entry in layout[:first_solution_page - 1]:
    text = doc[entry["page"] - 1].get_text()
    assert "Suggested marking points" not in text
    assert "FINAL MARK SCHEMES /" not in text

for task in data["tasks"] + data["advanced"]:
    assert sum(mark for _, mark in task["rubric"]) == task["marks"], task["id"]
    question = next(entry for entry in questions if entry["task_id"] == task["id"])
    response = next(entry for entry in responses if entry["task_id"] == task["id"])
    assert response["page"] == question["page"] + 1, "Each question needs an immediate full answer page"
    question_text = "".join(doc[question["page"] - 1].get_text().split())
    assert "".join(task["question"].split()) in question_text, task["id"]
    response_page = doc[response["page"] - 1]
    writing_lines = []
    for drawing in response_page.get_drawings():
        for item in drawing["items"]:
            if item[0] != "l":
                continue
            start, end = item[1:3]
            if (abs(start.y - end.y) < 0.1
                    and 495 < abs(end.x - start.x) < 501
                    and 120 < start.y < response_page.rect.height - 55):
                writing_lines.append(start.y)
    assert len(writing_lines) == 36, (task["id"], len(writing_lines))
    assert max(writing_lines) - min(writing_lines) >= 590, "Answer lines must fill the printable page"
    assert "Suggested marking points" not in response_page.get_text()
    # Verify that the whole solution was typeset on its intended page.
    number = next(entry["page"] for entry in solutions if entry["task_id"] == task["id"])
    compact_page = "".join(doc[number - 1].get_text().split())
    for line in task["code"].splitlines():
        assert "".join(line.split()) in compact_page, (task["id"], line)

report = {
    "file": pdf.name,
    "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "pages": len(doc),
    "core_tasks": len(data["tasks"]),
    "advanced_tasks": len(data["advanced"]),
    "dedicated_full_answer_pages": len(responses),
    "writing_lines_per_answer_page": 36,
    "final_mark_scheme_pages": [first_solution_page, len(doc)],
    "suggested_marks": sum(t["marks"] for t in data["tasks"] + data["advanced"]),
    "checks": {
        "expected_pagination": "passed",
        "pdf_navigation": "passed",
        "page_footers": "passed",
        "searchable_text_and_assignment_arrows": "passed",
        "text_within_page_and_above_footer": "passed",
        "complete_solution_code_on_expected_pages": "passed",
        "one_full_answer_page_immediately_after_every_question": "passed",
        "36_full_width_writing_lines_per_answer_page": "passed",
        "all_mark_schemes_in_final_section": "passed",
        "mark_allocations": "passed",
    },
    "review_notes": [
        "Rendered samples of revised question pages, full answer pages and final mark schemes were visually inspected.",
        "Worked solutions and listed boundary cases were manually reviewed; automated checks here cover the PDF and marking totals, not pseudocode execution.",
    ],
}
(ROOT / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
