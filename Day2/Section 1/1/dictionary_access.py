def demonstrate_dict_access():
    user = {"name": "Alice"}

    # Using .get() to access an existing key
    name = user.get("name")
    print("Name (using .get()):", name)

    # Using .get() to access a non-existing key with a default value
    age = user.get("age", "Unknown")
    print("Age (using .get() with default):", age)

    # Using .setdefault() to access an existing key (it won't change the value)
    user_age = user.setdefault("age", 30)
    print("Age (using .setdefault()):", user_age)
    print("Updated user dictionary:", user)

    # Using .setdefault() to add a new key with a default value
    user.setdefault("city", "Delhi")
    print("Updated user dictionary after setdefault:", user)

if __name__ == "__main__":
    demonstrate_dict_access()
