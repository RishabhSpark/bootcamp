def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        raise

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Reraised: {e}")