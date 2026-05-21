from datetime import date, timedelta


def date_range(start, end, step=1, fmt=None):
    current = start
    delta = timedelta(days=step)
    while current <= end:
        yield current.strftime(fmt) if fmt else current
        current += delta


# Use case: generate all dates for a monthly report
start = date(2025, 1, 1)
end = date(2025, 1, 10)

print("\n\nGenerator — every 3 days:")
for checkpoint in date_range(start, end, step=3):
    print(checkpoint, end="  ")

print("\n\nGenerator — custom format:")
for label in date_range(start, end, step=3, fmt="%d %b %Y"):
    print(label, end="  ")
