import streamlit as st
import matplotlib.pyplot as plt

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- REPORT FUNCTION ----------------
def generate_report(issues, total_lines, blank_lines, comment_lines, code_lines):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Static Code Analyzer Report", styles["Title"]))
    content.append(Spacer(1, 10))

    # Metrics
    content.append(Paragraph(f"Total Lines: {total_lines}", styles["Normal"]))
    content.append(Paragraph(f"Blank Lines: {blank_lines}", styles["Normal"]))
    content.append(Paragraph(f"Comment Lines: {comment_lines}", styles["Normal"]))
    content.append(Paragraph(f"Code Lines: {code_lines}", styles["Normal"]))
    content.append(Spacer(1, 10))

    # Issues
    content.append(Paragraph("Issues Found:", styles["Heading2"]))

    if issues:
        for i, issue in enumerate(issues, 1):
            content.append(Paragraph(f"{i}. {issue}", styles["Normal"]))
    else:
        content.append(Paragraph("No issues found", styles["Normal"]))

    doc.build(content)

# ---------------- TITLE ----------------
st.title("💻 Static Code Analyzer")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📂 Upload your code file", 
    type=["py", "cpp", "java", "js"]
)

# ---------------- MAIN LOGIC ----------------
if uploaded_file:
    code = uploaded_file.read().decode("utf-8")

    # ---------------- ISSUE DETECTION ----------------
    issues = []

    if "print(" in code:
        issues.append("Debug print statement found")

    if "import *" in code:
        issues.append("Avoid using 'import *'")

    if "var " in code:
        issues.append("Use 'let' or 'const' instead of 'var' (JS)")

    if "==" in code:
        issues.append("Check usage of '==' (may need '===')")

    # ---------------- LINE ANALYSIS ----------------
    lines = code.split("\n")

    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == "")

    # Detect comments
    comment_lines = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or stripped.startswith("//") or "/*" in stripped or "*/" in stripped:
            comment_lines += 1

    code_lines = total_lines - blank_lines - comment_lines

    # ---------------- DISPLAY ISSUES ----------------
    st.subheader("📋 Issues Found")

    if issues:
        for issue in issues:
            st.warning(issue)
    else:
        st.success("No major issues found")

    # ---------------- DISPLAY METRICS ----------------
    st.subheader("📊 Code Analysis")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Lines", total_lines)
    col2.metric("Blank Lines", blank_lines)
    col3.metric("Comment Lines", comment_lines)
    col4.metric("Code Lines", code_lines)

    # ---------------- GRAPH ----------------
    st.subheader("📉 Code Graph")

    fig, ax = plt.subplots()

    labels = ["Code", "Blank", "Comments", "Issues"]
    values = [code_lines, blank_lines, comment_lines, len(issues)]

    ax.bar(labels, values)
    ax.set_title("Code Overview")

    st.pyplot(fig)

    # ---------------- PDF REPORT ----------------
    st.subheader("📄 Download Report")

    if st.button("Generate PDF Report"):
        generate_report(issues, total_lines, blank_lines, comment_lines, code_lines)

        with open("report.pdf", "rb") as file:
            st.download_button(
                label="⬇ Download Report",
                data=file,
                file_name="code_report.pdf",
                mime="application/pdf"
            )