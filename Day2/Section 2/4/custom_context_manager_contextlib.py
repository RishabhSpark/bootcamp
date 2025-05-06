from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed: {end - start:.4f} seconds")

with timer():
    sum(i for i in range(1000000))