def walrus_operator_example():
    while (line := input("Enter something: ")) != "exit":
        print(f"You entered: {line}")

walrus_operator_example()