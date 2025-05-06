def process_number(value: object) -> int:
    if isinstance(value, int):
        return value * 2
    else:
        return "Invalid input, expected an integer."

print(process_number(5))
print(process_number("5"))