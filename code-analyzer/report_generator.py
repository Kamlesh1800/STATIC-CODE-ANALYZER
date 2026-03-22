from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(issues):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("Code Analysis Report", styles["Title"]))

    for issue in issues:
        content.append(Paragraph(issue, styles["Normal"]))

    doc.build(content)