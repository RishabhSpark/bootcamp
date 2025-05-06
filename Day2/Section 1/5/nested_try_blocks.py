try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Outer Error: {e}")
    try:
        x = int("abc")
    except ValueError as inner_e:
        print(f"Inner Error: {inner_e}")