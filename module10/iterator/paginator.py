class PaginatedResults:
    def __init__(self, records, page_size=3):
        self.records = records
        self.page_size = page_size
        self.offset = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.offset >= len(self.records):
            raise StopIteration
        page = self.records[self.offset : self.offset + self.page_size]
        self.offset += self.page_size
        return page


def paginate(records, page_size=3):
    for offset in range(0, len(records), page_size):
        yield records[offset : offset + page_size]


# Use case: process a large set of DB records in batches
# without loading everything into memory at once
orders = [f"order_{i:03d}" for i in range(1, 22)]

print("Class:")
for page_num, batch in enumerate(PaginatedResults(orders, page_size=5), 1):
    print(f"  Page {page_num}: {batch}")

print("\nGenerator:")
for page_num, batch in enumerate(paginate(orders, page_size=5), 1):
    print(f"  Page {page_num}: {batch}")
