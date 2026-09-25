"""Build the contact-free public PDF from the resume section of index.html.

Requires reportlab. The private application resume is maintained separately.
"""

from html import escape
from html.parser import HTMLParser
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


class ResumeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.entries = []
        self.entry = None
        self.capture = None
        self.buffer = []

    def handle_starttag(self, tag, attrs):
        if tag == "article" and "resume-entry" in dict(attrs).get("class", "").split():
            self.entry = []
        if self.entry is not None and tag in {"h3", "p", "li"}:
            self.capture = tag
            self.buffer = []

    def handle_data(self, data):
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if self.capture == tag:
            value = " ".join("".join(self.buffer).split()).replace("–", "-")
            self.entry.append((tag, value))
            self.capture = None
        if tag == "article" and self.entry is not None:
            self.entries.append(self.entry)
            self.entry = None


root = Path(__file__).resolve().parents[1]
parser = ResumeParser()
parser.feed((root / "index.html").read_text())
if len(parser.entries) != 5:
    raise ValueError("Expected experience, experience, project, skills, and education entries")

body = ParagraphStyle("Body", fontName="Helvetica", fontSize=10.3, leading=13.1, spaceAfter=4)
heading = ParagraphStyle("Heading", parent=body, fontName="Helvetica-Bold", fontSize=10,
                         spaceBefore=10, spaceAfter=5)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=10, firstLineIndent=0, bulletIndent=0)
name = ParagraphStyle("Name", parent=body, fontName="Helvetica-Bold", fontSize=21, leading=24, spaceAfter=4)
links = ParagraphStyle("Links", parent=body, fontSize=9.4, leading=12, spaceAfter=7)
role = ParagraphStyle("Role", parent=body, fontName="Helvetica-Bold", spaceAfter=0)
dates = ParagraphStyle("Dates", parent=body, fontSize=9.4, alignment=TA_RIGHT, spaceAfter=0)
story = [
    Paragraph("Harrison O'Connor-Hoover", name),
    Paragraph('<link href="https://harrisonoconnorhoover.com" color="#0000ee">harrisonoconnorhoover.com</link> | '
              '<link href="https://github.com/harrisonoconnorhover" color="#0000ee">GitHub</link> | '
              '<link href="https://www.linkedin.com/in/harrison-o-810b6322b/" color="#0000ee">LinkedIn</link>', links),
    Paragraph("<b>GTM Engineering and Revenue Systems</b>", body),
    Paragraph("GTM Engineer with 4+ years building CRM automation, API integrations, and AI-assisted workflows. "
              "Own 20+ production HubSpot systems, with Salesforce consulting across 15 B2B client accounts.", body),
    Paragraph("PROFESSIONAL EXPERIENCE", heading),
]

for entry in parser.entries[:2]:
    titles = [text for tag, text in entry if tag == "h3"]
    details = [text for tag, text in entry if tag == "p"]
    row = Table([[Paragraph(escape(f"{titles[0]} | {titles[1]}"), role),
                  Paragraph(escape(f"{details[1]} | {details[0]}"), dates)]], colWidths=[266, 259])
    row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 0),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story.append(row)
    for tag, text in entry:
        if tag == "li":
            story.append(Paragraph(escape(text), bullet, bulletText="•"))
    story.append(Spacer(1, 3))

project = parser.entries[2]
story.append(Paragraph("SELECTED INDEPENDENT PROJECT", heading))
project_name = [text for tag, text in project if tag == "h3"][1]
project_description = [text for tag, text in project if tag == "p"][-1]
story.append(Paragraph('<link href="https://gtm-control-tower.pages.dev/#salesforce-proof" color="#0000ee"><b>'
                       + escape(project_name) + "</b></link> | " + escape(project_description), body))
story.append(Paragraph("TECHNICAL SKILLS", heading))
for tag, text in parser.entries[3]:
    if tag == "p":
        label, value = text.split(":", 1)
        story.append(Paragraph(f"<b>{escape(label)}:</b>{escape(value)}", body))

education = parser.entries[4]
degree = [text for tag, text in education if tag == "h3"][1]
education_details = [text for tag, text in education if tag == "p"]
story.append(Paragraph("EDUCATION", heading))
story.append(Paragraph(escape(f"{degree} | {education_details[1]} | {education_details[0]}"), body))

output = root / "assets" / "Harrison_OConnor-Hoover_Resume.pdf"
SimpleDocTemplate(str(output), pagesize=letter, leftMargin=43.5, rightMargin=43.5,
                  topMargin=36, bottomMargin=36, title="Harrison O'Connor-Hoover - GTM Engineering",
                  author="Harrison O'Connor-Hoover").build(story)
print(output)
