# Pseudocode Workbook — Computer Science 9618

An original, independent 56-page workbook for learners practising Cambridge International Computer Science 9618 pseudocode.

**[Open or download the PDF](Pseudocode-Workbook-9618.pdf)**

Includes:

- Notation reminders, control-flow guidance and a fully worked trace.
- Twelve core tasks covering input, selection, validation, loops, strings, arrays, searching, sorting, functions and records.
- Four advanced tasks covering recursion, stack removal, circular queue insertion and sequential text files.
- A separate question page and a dedicated full lined answer page for every task, with 36 writing lines on each answer page.
- All sixteen worked answers, test cases and mark schemes together at the end (pages 41–56).
- Teacher guidance and links to the official notation guides.

All questions, explanations and marking points were written for this workbook. It is not a reproduction of the Scribd publication and contains no copied past-paper questions or official mark schemes. It is not endorsed by Cambridge International. Use the official syllabus and notation guide for your examination year.

## Editable files

- `workbook.json`: questions, answers, tests and marking points.
- `Workbook-Source.md`: a readable export of the tasks and answers.
- `build.py`: PDF layout, reference pages, worked trace and teacher guidance.
- `validation.json`: PDF structure and layout validation results.
- `validate.py`: repeatable PDF validation (requires `pymupdf`).
- `page-layout.json`: page roles and question, answer-page and mark-scheme locations.

## Rebuild

Requires Python 3.10+ and the DejaVu Sans / DejaVu Sans Mono TrueType fonts. On Debian or Ubuntu the fonts are provided by `fonts-dejavu-core`. If using a different operating system, update the font paths near the start of `build.py`.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python build.py
```

The build checks each marking total and rejects code lines wider than their container. It writes both the PDF and Markdown export.

Optional PDF validation:

```bash
.venv/bin/pip install pymupdf
.venv/bin/python validate.py
```

Validation checks pagination, page navigation, footers, searchable text, text boundaries, complete solution listings and marking totals. It also verifies that every question is followed by a full answer page with 36 writing lines and that every mark scheme is in the final section. Algorithm behaviour and the printed edge cases were manually reviewed; the validation script does not execute pseudocode.

## Official notation references

- [2026 pseudocode guide](https://www.cambridgeinternational.org/Images/697401-2026-pseudocode-guide-for-teachers.pdf)
- [2027–2029 pseudocode guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf)
- [Computer Science 9618 qualification page](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/)

Prepared November 2026.
