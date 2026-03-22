def analyze_cpp(code):
    issues = []

    if "using namespace std" in code:
        issues.append("Avoid using 'using namespace std'")

    if "cout <<" in code:
        issues.append("Debug output (cout) found")

    if "int global" in code or "globalVar" in code:
        issues.append("Global variable detected")

    if "==" in code:
        issues.append("Check proper comparison usage")

    return issues