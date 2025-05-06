x = 10  # Global variable

def modify_global():
    global x  # Declare the global variable
    x = 20    # Modify the global variable
    print(f"Global x inside function: {x}")

modify_global()
print(f"Global x after function call: {x}")