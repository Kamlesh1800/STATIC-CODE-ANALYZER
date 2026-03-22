def analyze_js(code):
    issues = []

    if "var " in code:
        issues.append("Use 'let' or 'const' instead of 'var'")

    if "console.log" in code:
        issues.append("Console log found")

    if "==" in code:
        issues.append("Use '===' instead of '=='")

    if "function" in code and "return" not in code:
        issues.append("Function missing return statement")

    return issues