def safe_convert_to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        return 0  # Return 0 if conversion fails

print(safe_convert_to_int("123"))
print(safe_convert_to_int("abc"))