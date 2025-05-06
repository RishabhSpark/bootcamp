def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Usage
for num in countdown(5):
    print(num)