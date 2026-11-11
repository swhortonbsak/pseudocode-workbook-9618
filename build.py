#!/usr/bin/env python3
"""Build the original workbook from editable JSON using ReportLab."""
import html
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Preformatted, Flowable,
)

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "workbook.json").read_text())
OUT = ROOT / "Pseudocode-Workbook-9618.pdf"
NAVY = colors.HexColor("#15304B")
TEAL = colors.HexColor("#007F83")
INK = colors.HexColor("#213448")
MUTED = colors.HexColor("#516578")
PALE = colors.HexColor("#EDF6F6")
GREY = colors.HexColor("#F3F5F8")
RULE = colors.HexColor("#CBD6DE")

for name, filename in [
    ("Body", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ("Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ("Mono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, filename))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Bold", italic="Body", boldItalic="Bold")

S = {
    "body": ParagraphStyle("body", fontName="Body", fontSize=9.5, leading=14, textColor=INK, spaceAfter=8),
    "small": ParagraphStyle("small", fontName="Body", fontSize=8.2, leading=11.7, textColor=MUTED, spaceAfter=5),
    "h1": ParagraphStyle("h1", fontName="Bold", fontSize=22, leading=27, textColor=NAVY, spaceAfter=12),
    "h2": ParagraphStyle("h2", fontName="Bold", fontSize=12.2, leading=16, textColor=TEAL, spaceBefore=8, spaceAfter=7),
    "label": ParagraphStyle("label", fontName="Bold", fontSize=8, leading=11, textColor=TEAL, spaceAfter=7),
    "code": ParagraphStyle("code", fontName="Mono", fontSize=8.1, leading=10.8, textColor=INK),
    "cell": ParagraphStyle("cell", fontName="Body", fontSize=8.3, leading=12, textColor=INK),
    "cover": ParagraphStyle("cover", fontName="Bold", fontSize=38, leading=44, textColor=NAVY, spaceAfter=22),
}
WIDTH = A4[0] - 96
story = []
page_titles = []
page_layout = []

def p(text, style="body"):
    return Paragraph(html.escape(str(text)).replace("\n", "<br/>"), S[style])

def rich(text, style="body"):
    return Paragraph(text, S[style])

def code(text):
    # Keep every statement at its original indentation. Fail rather than clip.
    for line in text.splitlines():
        assert pdfmetrics.stringWidth(line, "Mono", 8.1) < WIDTH - 22, line
    pre = Preformatted(text, S["code"])
    t = Table([[pre]], colWidths=[WIDTH])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREY),
        ("BOX", (0, 0), (-1, -1), 0.4, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t

def table(rows, widths=None, header=True):
    cells = [[p(c, "cell") for c in row] for row in rows]
    t = Table(cells, colWidths=widths or [WIDTH / len(rows[0])] * len(rows[0]), hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -1), 0.35, RULE),
    ]
    if header:
        commands.append(("BACKGROUND", (0, 0), (-1, 0), PALE))
    t.setStyle(TableStyle(commands))
    return t

class WritingLines(Flowable):
    def __init__(self, count=6, gap=14):
        Flowable.__init__(self)
        self.width, self.height, self.count, self.gap = WIDTH, count * gap, count, gap
    def draw(self):
        self.canv.setStrokeColor(RULE)
        self.canv.setLineWidth(0.35)
        for n in range(self.count):
            y = self.height - (n + 1) * self.gap + 3
            self.canv.line(0, y, self.width, y)

def page(title, items, label="LEARN / PRACTISE / REVIEW", cover=False,
         role="reference", task_id=None):
    if story:
        story.append(PageBreak())
    page_titles.append(title)
    page_layout.append({"page": len(page_titles), "title": title,
                        "role": role, "task_id": task_id})
    if not cover:
        story.extend([p(label, "label"), p(title, "h1")])
    story.extend(items)

def rubric(task):
    return table([["Suggested marking points", "Marks"]] + task["rubric"], [WIDTH - 50, 50])

page("Pseudocode Workbook", [
    Spacer(1, 48),
    p("COMPUTER SCIENCE / 9618", "label"),
    p("Pseudocode\nWorkbook", "cover"),
    p("From confident foundations to advanced algorithm practice", "h2"),
    p(DATA["subtitle"]),
    Spacer(1, 25),
    table([
        ["12 core tasks", "4 advanced tasks"],
        ["Worked solutions and test cases", "Suggested marks and teacher notes"],
        ["A full answer page for every task", "All mark schemes at the end"],
    ], header=False),
    Spacer(1, 30),
    p("Name: __________________________________________________"),
    p("Class: ____________________    Date: ____________________"),
    Spacer(1, 38),
    p(DATA["edition"], "small"),
    p("An independent learning resource. Questions, explanations and mark allocations were written for this workbook. This publication is not endorsed by Cambridge International and is not a reproduction of the Scribd workbook.", "small"),
], cover=True)

core_marks = sum(t["marks"] for t in DATA["tasks"])
advanced_marks = sum(t["marks"] for t in DATA["advanced"])
page("How to use this workbook", [
    p("Read the reference pages and trace the worked example, then attempt the tasks. Each question has planning space and is followed immediately by a dedicated full lined answer page. All worked solutions and mark schemes are collected at the end of the PDF."),
    table([
        ["Section", "Pages", "Purpose"],
        ["Notation and control flow", "3–4", "Read and write consistent pseudocode"],
        ["Worked trace and data structures", "5–6", "See how state changes during execution"],
        ["Core questions and answer pages", "7–30", "One question and one full answer page per task"],
        ["Advanced questions and answer pages", "31–38", "Recursion, stack, queue and text files"],
        ["Teacher guidance and references", "39–40", "Assess, reteach and extend"],
        ["Final mark schemes: tasks 1–12", "41–52", "Core solutions, tests and marking points"],
        ["Final mark schemes: tasks 13–16", "53–56", "Advanced solutions, tests and marking points"],
    ], [WIDTH * 0.40, WIDTH * 0.12, WIDTH * 0.48]),
    p("A useful practice cycle", "h2"),
    p("1. State the inputs, outputs and assumptions.\n2. Choose the data and control structures.\n3. Write an algorithm with clear indentation.\n4. Trace a normal case and a boundary case.\n5. Compare with the suggested solution and explain any differences."),
    p("Levels and scope", "h2"),
    p("Tasks 1–12 build from introductory programming towards AS algorithm work. Tasks 13–16 are advanced practice, including A2-style data-structure operations. The workbook is a focused practice resource rather than a complete course or a past-paper collection."),
    p(f"Core tasks: {core_marks} suggested marks. Advanced tasks: {advanced_marks} suggested marks. Total: {core_marks + advanced_marks}. These allocations are for classroom feedback; they are not official Cambridge mark schemes."),
    p("Conventions", "h2"),
    p("Inputs have the stated types. Validate only when a question asks for it. Supplied arrays and global state already exist; declarations marked as supplied are explanatory comments. Array bounds are inclusive. Each test row represents a separate run unless stated otherwise."),
])

page("Notation at a glance", [
    p("Use descriptive identifiers, capitalised keywords and indentation that shows which statements belong together. The following are syntax reminders; the examples throughout this workbook are original."),
    table([
        ["Idea", "Example / meaning"],
        ["Declaration", "DECLARE Balance : REAL"],
        ["Constant", "CONSTANT Capacity = 12"],
        ["Assignment", "Balance ← Balance + 2.50"],
        ["Input / output", "INPUT Balance; OUTPUT Balance (write on separate lines)"],
        ["Integer / real", "INTEGER stores whole numbers; REAL can hold fractions"],
        ["Text / truth", "STRING for text; CHAR for a character; BOOLEAN for TRUE or FALSE"],
        ["Comparison", "=, <>, <, <=, >, >= produce a Boolean result"],
        ["Logic", "AND, OR, NOT combine or invert Boolean values"],
        ["Division", "17 / 5 gives 3.4; 17 DIV 5 gives 3; 17 MOD 5 gives 2"],
        ["Joining strings", "\"Unit\" & \"-\" & \"4\" produces \"Unit-4\""],
        ["Comment", "// Explain an assumption or purpose"],
    ], [WIDTH * 0.28, WIDTH * 0.72]),
    p("Assignment and comparison have different jobs", "h2"),
    code("DECLARE Points : INTEGER\nPoints ← 7\nIF Points = 7 THEN\n   OUTPUT \"Target reached\"\nENDIF"),
    p("The arrow changes Points. The equality test asks a question about its current value. A variable must have a value before an expression uses it."),
    p("String helpers used here", "h2"),
    p("LENGTH(S) counts characters. MID(S, Start, Count) extracts Count characters starting at the 1-based position Start. Each string task states the helpers it allows."),
])

page("Choose the control structure", [
    p("Choose a structure based on what controls the next step: a condition, a fixed count, or the arrival of a stopping value."),
    table([
        ["Structure", "Choose it when…", "Boundary to check"],
        ["IF / ELSE", "One of two actions is needed", "Equality at the threshold"],
        ["FOR / NEXT", "The iteration range is known", "First and last iteration"],
        ["WHILE", "The body may run zero times", "Condition false initially"],
        ["REPEAT / UNTIL", "The body must run at least once", "Condition true after first run"],
    ], [100, 220, WIDTH - 320]),
    p("Count a known range", "h2"),
    code("DECLARE Step : INTEGER\nFOR Step ← 2 TO 8 STEP 2\n   OUTPUT Step\nNEXT Step"),
    p("This outputs 2, 4, 6, 8. NEXT Step closes the FOR loop. STEP is optional when the increment is 1."),
    p("Repeat until an input is valid", "h2"),
    code("DECLARE Size : INTEGER\nREPEAT\n   INPUT Size\nUNTIL (Size >= 1) AND (Size <= 6)\nOUTPUT Size"),
    p("The condition means stop when Size is within the inclusive range. Inputs 0, 7, 6 require three attempts and produce 6."),
    p("Remember the stopping rule", "h2"),
    p("A valid first input ends this REPEAT loop after one attempt. A WHILE loop checks its condition before running the body, so variables used in that condition must already have values. Every input loop needs a way to read a new value and eventually meet its stopping condition."),
])

page("Worked example: filter and total", [
    p("Read INTEGER values until 0. Add only positive values and count how many were added. Output Total and Count. Negative values are ignored."),
    code("DECLARE Value, Total, Count : INTEGER\nTotal ← 0\nCount ← 0\nINPUT Value\nWHILE Value <> 0\n   IF Value > 0 THEN\n      Total ← Total + Value\n      Count ← Count + 1\n   ENDIF\n   INPUT Value\nENDWHILE\nOUTPUT Total, Count"),
    p("Trace for inputs 6, -2, 9, 0", "h2"),
    table([
        ["Input", "Action", "Total after action", "Count after action"],
        ["—", "Initialise", "0", "0"],
        ["6", "Include", "6", "1"],
        ["-2", "Ignore", "6", "1"],
        ["9", "Include", "15", "2"],
        ["0", "Stop before body", "15", "2"],
    ], [55, 155, 145, WIDTH - 355]),
    p("Why this works", "h2"),
    p("After each processed value, Total is the sum of the positive values seen so far and Count is their number. Initialising both to zero makes that statement true before any values are processed. The sentinel is tested before the body, so it contributes nothing."),
    p("Check another route", "h2"),
    p("For inputs -3, -1, 0, both outputs are 0. If the first input is 0, the loop runs zero times and both outputs are also 0. The final INPUT inside the body is essential: it moves the algorithm towards the sentinel."),
])

page("Arrays, modules and file state", [
    p("An algorithm becomes easier to reason about when its data has clear bounds and each module has one defined responsibility."),
    p("Declare the shape, then respect the bounds", "h2"),
    code("DECLARE Levels : ARRAY[1:12] OF INTEGER\nDECLARE Grid : ARRAY[1:3,1:4] OF INTEGER\nDECLARE Index : INTEGER\nFOR Index ← 1 TO 12\n   Levels[Index] ← 0\nNEXT Index"),
    p("An array's capacity and its used length may differ. If N entries are used in Levels, process 1 to N rather than all 12. A zero used length means there is no valid used element to inspect."),
    p("Return a value or perform an action", "h2"),
    code("FUNCTION AddFee(Price : REAL) RETURNS REAL\n   RETURN Price + 1.25\nENDFUNCTION\n\nPROCEDURE ShowReceipt(Amount : REAL)\n   OUTPUT \"Amount: \", Amount\nENDPROCEDURE\n\nCALL ShowReceipt(AddFee(8.00))"),
    p("A function call belongs inside an expression; a procedure is invoked using CALL. A BYREF parameter allows the called module to change the caller's variable. Otherwise parameters here are passed by value."),
    p("File lifecycle", "h2"),
    p("Open a file in its required mode, read or write, then close it. For sequential reading, test EOF before READFILE. READFILE gives a STRING for one line. WRITE mode replaces an existing file; APPEND adds to its end."),
    p("State safety", "h2"),
    p("Check empty and full conditions before using a stack or queue slot. Test a string's length before extracting a fixed prefix. Place potentially unsafe accesses inside a guarded branch rather than assuming AND will skip an operand."),
])

for task in DATA["tasks"] + DATA["advanced"]:
    level = "CORE" if task["id"] <= 12 else "ADVANCED"
    question_page = len(page_titles) + 1
    page(f"{task['id']:02d} / {task['title']}", [
        p(f"{task['topic']}  •  {task['marks']} suggested marks", "small"),
        p(task["question"]),
        p("Planning prompt", "h2"),
        p(task.get("hint", task.get("scaffold", ""))),
        p("Planning and first draft", "h2"),
        p(f"Use this space to plan. A full lined answer page for this question follows on page {question_page + 1}.", "small"),
        WritingLines(19, 17),
    ], f"PRACTISE / {level} QUESTION", role="question", task_id=task["id"])
    page(f"Question {task['id']:02d} / answer", [
        p(task["title"], "small"),
        p("Write your pseudocode, explanations and test traces here.", "small"),
        WritingLines(36, 17),
    ], "STUDENT RESPONSE / FULL ANSWER PAGE", role="response", task_id=task["id"])

page("Teacher guidance", [
    p("Suggested teaching sequence", "h2"),
    p("Use tasks 1–4 to establish sequence, selection and controlled input. Use 5–7 for array and string traversal. Follow with 8–10 for search and sort, then 11–12 for modular design and record access. Teach the state conventions explicitly before assigning advanced stack and queue tasks."),
    p("Assess the algorithm's behaviour", "h2"),
    p("The marking points are independent classroom suggestions. Award each point once when the relevant behaviour is correct. Accept alternative correct algorithms unless a task specifies the method, such as bubble sort, binary search or recursion. Do not award a correct-output point for an algorithm that only happens to work on the displayed example."),
    p("Use targeted feedback", "h2"),
    table([
        ["Observed issue", "Useful follow-up"],
        ["Uninitialised accumulator", "Ask for the value before the first input"],
        ["Off-by-one error", "Trace N = 0, N = 1 and the final used index"],
        ["Incorrect threshold", "Test the boundary and values either side"],
        ["Sentinel included in data", "Mark exactly when the stopping input is tested"],
        ["Incorrect empty/full operation", "Record state before and after a failed call"],
        ["Non-terminating search/recursion", "Identify the quantity that must get smaller"],
    ], [WIDTH * 0.43, WIDTH * 0.57]),
    p("Differentiate with purpose", "h2"),
    p("Support: supply declarations, a trace-table heading, or the first loop condition. Ask students to explain each state change aloud. Extend: require an invariant, compare linear and binary search conditions, or derive the worst-case number of passes for a sorting method."),
    p("Feedback record", "h2"),
    p("One strength: __________________________________________________\n\nOne correction: _________________________________________________\n\nA test that exposed it: ____________________________________________"),
])

page("References and next steps", [
    p("Official notation references", "h2"),
    p("The official guides were consulted for notation: assignment arrows, array bounds, NEXT, function return syntax, BYREF parameters and sequential file commands. The teaching explanations, scenarios, solutions and marking points in this workbook are original."),
    rich('<b>For examinations in 2026:</b><br/><link href="https://www.cambridgeinternational.org/Images/697401-2026-pseudocode-guide-for-teachers.pdf" color="#007F83">Cambridge International 9618 Pseudocode Guide for Teachers (2026)</link>'),
    rich('<b>For examinations in 2027–2029:</b><br/><link href="https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf" color="#007F83">Cambridge International 9618 Pseudocode Guide (2027–2029)</link>'),
    rich('<b>Qualification and syllabus information:</b><br/><link href="https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/" color="#007F83">Cambridge International AS &amp; A Level Computer Science (9618)</link>'),
    p("Use the syllabus and notation guide for your own examination year. This resource focuses on selected algorithm skills; it does not claim to cover every assessed topic."),
    p("Independent resource statement", "h2"),
    p("This workbook was created in response to a request for a new pseudocode resource. It is not a copy, transcription or reformatting of the linked Scribd publication. It contains no official Cambridge past-paper questions or official mark schemes. Cambridge International and other names belong to their respective owners."),
    p("Continue your practice", "h2"),
    p("Choose one solution and translate it into your programming language. Run every listed test and add one new edge case. Then change one requirement, update the algorithm, and explain which statements must change and why."),
    p("Choose a next practice target", "h2"),
    p("Return to a task that needed correction and attempt it again on its full answer page. Use a different test case to check the revised algorithm before comparing it with the final mark scheme."),
    Spacer(1, 17),
    p("Editable source: workbook.json and build.py. Rebuild instructions are in README.md. Prepared November 2026.", "small"),
])

for task in DATA["tasks"] + DATA["advanced"]:
    level = "CORE" if task["id"] <= 12 else "ADVANCED"
    page(f"{task['id']:02d} / {task['title']}", [
        p(f"{task['topic']}  •  {task['marks']} suggested marks", "small"),
        code(task["code"]),
        Spacer(1, 8),
        p(task["explanation"]),
        table([["Test input / state", "Expected result"]] + task["tests"]),
        Spacer(1, 9),
        rubric(task),
        Spacer(1, 9),
        p("Common error: " + task["pitfall"], "small"),
    ], f"FINAL MARK SCHEMES / {level} WORKED SOLUTION",
       role="solution", task_id=task["id"])

def decorate(canvas, doc):
    canvas.saveState()
    w, h = A4
    if doc.page > 1:
        canvas.setStrokeColor(TEAL)
        canvas.setLineWidth(2)
        canvas.line(48, h - 36, w - 48, h - 36)
        canvas.setFont("Body", 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(48, h - 28, "PSEUDOCODE WORKBOOK / COMPUTER SCIENCE 9618")
    else:
        canvas.setFillColor(TEAL)
        canvas.rect(0, h - 14, w, 14, fill=1, stroke=0)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(48, 41, w - 48, 41)
    canvas.setFont("Body", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, 28, "Independent resource • Original questions • Suggested classroom marks")
    canvas.setFont("Bold", 8)
    canvas.drawRightString(w - 48, 28, f"{doc.page:02d} / {len(page_titles)}")
    if doc.page <= len(page_titles):
        key = f"page-{doc.page}"
        canvas.bookmarkPage(key)
        canvas.addOutlineEntry(page_titles[doc.page - 1], key, level=0)
    canvas.restoreState()

def export_markdown():
    text = ["# " + DATA["title"], "", DATA["subtitle"], "", DATA["edition"], "",
            "Original independent practice; not endorsed by Cambridge International.", "",
            "For notation, control-flow explanations, the worked trace and teacher notes, see build.py or the PDF.", ""]
    for section, tasks in [("Core questions", DATA["tasks"]), ("Advanced questions", DATA["advanced"])]:
        text += ["## " + section, ""]
        for t in tasks:
            text += [f"### {t['id']}. {t['title']} ({t['marks']} marks)", "", t["question"], "",
                     "Planning prompt: " + t.get("hint", t.get("scaffold", "")), "",
                     "A dedicated full lined answer page follows this question in the PDF.", ""]
    text += ["## Final mark schemes and worked solutions", ""]
    for t in DATA["tasks"] + DATA["advanced"]:
        text += [f"### {t['id']}. {t['title']} ({t['marks']} marks)", "",
                 "```text", t["code"], "```", "", t["explanation"], "", "#### Test cases", ""]
        text += [f"- {a} → {b}" for a, b in t["tests"]]
        text += ["", "#### Suggested marking points", ""]
        text += [f"- {a}: {b} mark(s)" for a, b in t["rubric"]]
        text += ["", "Common error: " + t["pitfall"], ""]
    (ROOT / "Workbook-Source.md").write_text("\n".join(text))

if __name__ == "__main__":
    assert len(page_titles) == 56
    for task in DATA["tasks"] + DATA["advanced"]:
        assert sum(m for _, m in task["rubric"]) == task["marks"], task["id"]
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=48, leftMargin=48,
                            topMargin=57, bottomMargin=55, title=DATA["title"] + " | Computer Science 9618",
                            author="Independent Computer Science Learning Resources",
                            subject="Original pseudocode practice, worked solutions and teacher guidance")
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    export_markdown()
    (ROOT / "page-layout.json").write_text(json.dumps(page_layout, indent=2) + "\n")
    print(f"Built {OUT.name}; planned pages: {len(page_titles)}; marks: {core_marks + advanced_marks}")
