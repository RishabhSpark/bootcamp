def factorial(n, level=0):
    print(" " * level + f"Factorial({n}) called")
    if n == 1:
        return 1
    return n * factorial(n - 1, level + 1)

factorial(5)
