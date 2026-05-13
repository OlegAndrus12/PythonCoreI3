scores = [45, 72, 88, 60, 95]
normalized = list(map(lambda s: round(s / 100, 2), scores))
print(normalized)

prices = [10.0, 25.5, 8.99]
quantities = [3, 1, 5]
totals = list(map(lambda p, q: round(p * q, 2), prices, quantities))
print(totals)

tags = ["  python ", " flask ", "  sql  "]
clean_tags = list(map(str.strip, tags))
slugs = list(map(lambda t: t.strip().lower().replace(" ", "-"), tags))
print(clean_tags)
print(slugs)

records = [
    {"name": "alice", "score": 80},
    {"name": "bob", "score": 95},
    {"name": "carol", "score": 70},
]

labeled = list(map(lambda r: {**r, "grade": "A" if r["score"] >= 90 else "B"}, records))
print(labeled)
