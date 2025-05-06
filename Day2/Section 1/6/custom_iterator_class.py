class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current > self.n:
            raise StopIteration  # Stop iteration when count exceeds n
        current_value = self.current
        self.current += 1
        return current_value

counter = Counter(5)
for number in counter:
    print(number)