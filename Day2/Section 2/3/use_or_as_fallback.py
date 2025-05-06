def get_name() -> str:
    name = input("Enter your name: ") or "Anonymous"
    return name

print(get_name())
