import warnings

def divide(a, b):
    if b == 0:
        warnings.warn("Division by zero is not allowed, returning infinity")
        return float('inf')  # Return infinity as fallback
    return a / b

result = divide(10, 0)
