def outer_function():
    x = 10  # Variable in the outer function
    
    def inner_function():
        nonlocal x  # Access the 'x' variable from the outer function
        x = 20      # Modify it in the inner function
        print(f"Modified x inside inner function: {x}")
    
    inner_function()
    print(f"x in outer function after modification: {x}")

outer_function()