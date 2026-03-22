# Common rules for all languages

RULES = [
    {"name": "Too many lines", "check": lambda code: len(code.split("\n")) > 100},
    {"name": "Too many variables", "check": lambda code: code.count("=") > 20},
    {"name": "Long functions", "check": lambda code: code.count("def") > 10},
    {"name": "Too many loops", "check": lambda code: code.count("for") + code.count("while") > 10},
    {"name": "Magic numbers", "check": lambda code: any(num in code for num in ["123", "999", "111"])},
]

# Simulate 100+ rules
for i in range(1, 101):
    RULES.append({
        "name": f"Custom Rule {i}",
        "check": lambda code, i=i: len(code) % (i+2) == 0
    })