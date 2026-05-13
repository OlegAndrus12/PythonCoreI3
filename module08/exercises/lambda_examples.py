people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

by_age = sorted(people, key=lambda p: p["age"])
print(by_age)

students = [
    ("Alice", "B", 90),
    ("Bob", "A", 85),
    ("Charlie", "A", 92),
]

by_grade_then_score = sorted(students, key=lambda s: (s[1], -s[2]))
print(by_grade_then_score)


def apply(func, value):
    return func(value)

print(apply(lambda x: x ** 2, 5))
print(apply(lambda x: x.upper(), "hello"))

operations = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
}

for name, op in operations.items():
    print(f"{name}(4) = {op(4)}")
