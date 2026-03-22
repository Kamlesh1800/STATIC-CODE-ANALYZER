def analyze_cpp(code):
    issues = []

    if "using namespace std;" in code:
        issues.append("Avoid using 'using namespace std;'")

    if "cout <<" in code:
        issues.append("Debug output (cout) found")

    if "int " in code and "main" not in code:
        issues.append("Possible unnecessary variable")

    return issues