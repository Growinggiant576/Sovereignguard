"""Build the submission report (.docx) from docs/report_draft.md using the official template's styles.
usage: python3 docs/build_report.py <template.docx> <out.docx> [--phone "+.."]"""
import re, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT

tpl, out = sys.argv[1], sys.argv[2]
phone = sys.argv[sys.argv.index("--phone") + 1] if "--phone" in sys.argv else None
md = open("docs/report_draft.md", encoding="utf-8").read()
if phone:
    md = md.replace("Contact details: shafianwar745@gmail.com", f"Contact details: shafianwar745@gmail.com, {phone}")

doc = Document(tpl)
body = doc.element.body
for el in list(body):
    if not el.tag.endswith("sectPr"):
        body.remove(el)
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(1.6)
    s.left_margin = s.right_margin = Cm(1.8)
st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(9.5)
st.paragraph_format.space_after = Pt(3); st.paragraph_format.space_before = Pt(0)

def add_runs(par, text, size=None):
    for part in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = par.add_run(part[2:-2]); r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = par.add_run(part[1:-1]); r.font.name = "Consolas"
        else:
            r = par.add_run(part)
        if size: r.font.size = Pt(size)

def heading(text, level):
    p = doc.add_paragraph()
    r = p.add_run(text); r.bold = True
    r.font.size = Pt({0: 13, 1: 11, 2: 10}[level])
    p.paragraph_format.space_before = Pt(6 if level else 0); p.paragraph_format.space_after = Pt(2)

lines = md.splitlines(); i = 0
while i < len(lines):
    ln = lines[i].rstrip()
    if not ln: i += 1; continue
    if ln.startswith("# "): heading(ln[2:], 0)
    elif ln.startswith("## "): heading(ln[3:], 1)
    elif ln.startswith("### "): heading(ln[4:], 2)
    elif ln.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not all(re.fullmatch(r"-+", c) for c in cells): rows.append(cells)
            i += 1
        t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                cell = t.cell(r, c); cell.text = ""
                p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
                add_runs(p, f"**{val}**" if r == 0 and not val.startswith("**") else val, size=8)
        doc.add_paragraph().paragraph_format.space_after = Pt(0)
        continue
    elif re.match(r"^- ", ln):
        p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.first_line_indent = Cm(-0.3)
        add_runs(p, "\u2022 " + ln[2:]); p.paragraph_format.space_after = Pt(1)
    elif re.match(r"^\d+\. ", ln):
        p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.first_line_indent = Cm(-0.4)
        add_runs(p, ln); p.paragraph_format.space_after = Pt(1)
    else:
        p = doc.add_paragraph(); add_runs(p, ln)
    i += 1
doc.save(out); print("saved", out)
