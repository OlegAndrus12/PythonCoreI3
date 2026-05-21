from datetime import date, timedelta


class DateRangeIterator:
    def __init__(self, start, end, step=1, fmt=None):
        self.current = start
        self.end = end
        self.step = timedelta(days=step)
        self.fmt = fmt

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current.strftime(self.fmt) if self.fmt else self.current
        self.current += self.step
        return value


# Use case: generate all dates for a monthly report
start = date(2025, 1, 1)
end = date(2025, 1, 10)

print("Class — daily:")
for day in DateRangeIterator(start, end):
    print(day, end="  ")

print("\n\nClass — custom format:")
for day in DateRangeIterator(start, end, step=3, fmt="%d %b %Y"):
    print(day, end="  ")
