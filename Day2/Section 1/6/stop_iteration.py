def manual_iter():
    yield 1
    yield 2
    raise StopIteration("End of generator manually triggered.")

iterator = manual_iter()

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))  # Triggers StopIteration
except StopIteration as e:
    print(f"Caught StopIteration: {e}")