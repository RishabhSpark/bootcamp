def outer_function():
    x = 10

    def inner_function():
        print(f"Accessing x from outer function: {x}")

    inner_function()

outer_function()