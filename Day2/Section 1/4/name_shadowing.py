len = 5  # Shadowing the built-in len() function

# Try using the len() function
try:
    print(len([1, 2, 3]))  # This will throw an error because len() is now a variable
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'int' object is not callable

# Restoring the built-in len() function
del len

print(len([1, 2, 3]))