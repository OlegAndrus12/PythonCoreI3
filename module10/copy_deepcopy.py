import copy

employees = [
    {"name": "Alice", "email": "alice@company.com"},
    {"name": "Bob",   "email": "bob@company.com"},
]

# ── Shallow copy ───────────────────────────────────────────────────────────
shallow = copy.copy(employees)

print(employees is shallow)       # False — different list
print(employees[0] is shallow[0]) # True  — same dict objects inside

shallow[0]["email"] = "alice@personal.com"
print(employees[0]["email"])      # alice@personal.com — original changed too

# ── Deep copy ─────────────────────────────────────────────────────────────
employees[0]["email"] = "alice@company.com"  # reset

deep = copy.deepcopy(employees)

print(employees[0] is deep[0])    # False — different dict objects

deep[0]["email"] = "alice@personal.com"
print(employees[0]["email"])      # alice@company.com — original untouched
