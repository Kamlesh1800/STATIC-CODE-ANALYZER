def analyze_java(code):
    issues = []

    if "System.out.println" in code:
        issues.append("Debug print statement found")

    if "class" in code and "main" not in code:
        issues.append("Main method missing")

    if "==" in code:
        issues.append("Check object comparison (use .equals())")

    return issues