import re

def analyze_python(code):
    issues = []

    # 1. Avoid import *
    if "import *" in code:
        issues.append("Avoid using 'import *'")

    # 2. Debug print
    if "print(" in code:
        issues.append("Debug print statement found")

    # 3. Too many variables
    variables = re.findall(r'\b[a-zA-Z_]\w*\b', code)
    unique_vars = set(variables)

    if len(unique_vars) > 10:
        issues.append("Too many variables used")

    # 4. Long lines
    for line in code.split("\n"):
        if len(line) > 80:
            issues.append("Line exceeds 80 characters")
            break

    # 5. Unused variables (basic check)
    for var in unique_vars:
        if code.count(var) == 1:
            issues.append(f"Variable '{var}' declared but not used")

    return list(set(issues))   # remove duplicates