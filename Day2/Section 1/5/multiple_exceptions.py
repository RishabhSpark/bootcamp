try:
    # result = int("a")  # This will raise a ValueError
    result = 10 / 0  # This will raise a ZeroDivisionError
except ValueError:
    print("ValueError: Invalid value")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")
