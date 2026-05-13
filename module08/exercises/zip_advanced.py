from itertools import zip_longest

keys = ["name", "age", "city"]
values = ["Alice", 30, "Kyiv"]

profile = dict(zip(keys, values))
print(profile)

pairs = [(1, "a"), (2, "b"), (3, "c")]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85]

results = list(zip_longest(names, scores, fillvalue=0))
print(results)

items = ["apple", "banana", "cherry"]
prices = [1.2, 0.5, 2.0]

for i, (item, price) in enumerate(zip(items, prices)):
    print(f"{i + 1}. {item}: ${price}")

before = [10, 20, 30, 40]
after = [12, 18, 33, 40]

deltas = list(map(lambda pair: pair[1] - pair[0], zip(before, after)))
print(deltas)
