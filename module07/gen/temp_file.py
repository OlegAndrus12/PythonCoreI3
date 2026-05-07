import random
import tempfile
import os
from contextlib import contextmanager
from datetime import date, timedelta


STORES = ["Silpo", "Bolt", "Uklon"]


def generate_receipts(n=50):
    today = date.today()
    for i in range(n):
        spent_on = (today - timedelta(days=random.randint(0, 30)))
        store = random.choice(STORES)
        amount = round(random.uniform(10.0, 500.0), 2)
        yield f"RCP-{i:04d} | {spent_on} | {store:<12} | ${amount:.2f}\n"


@contextmanager
def temp_file(suffix=".txt"):
    fd, path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    try:
        with open(path, "w") as f: 
            yield f
    finally:
        if os.path.exists(path):
            os.remove(path)


def upload_to_s3(path, bucket="receipts"):
    size_kb = os.path.getsize(path) / 1024
    print(f"Uploading {path} ({size_kb:.1f} KB) to s3://{bucket}/...")
    # boto3.client("s3").upload_file(path, bucket, key)
    print("Upload complete.")


with temp_file() as f:
    f.writelines(generate_receipts(50))
    f.flush()
    upload_to_s3(f.name)
