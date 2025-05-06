def demonstrate_copying_pitfall():
    b = [1, 2, 3]
    
    # Reference assignment (both a and b point to the same list)
    a = b
    a.append(4)
    print("After a = b and appending 4:")
    print("a:", a)  # Output: [1, 2, 3, 4]
    print("b:", b)  # Output: [1, 2, 3, 4]
    
    # Slicing assignment (a gets a new list, changes don't affect b)
    a = b[:]
    a.append(5)  # This modifies only a
    print("\nAfter a = b[:] and appending 5:")
    print("a:", a)  # Output: [1, 2, 3, 5]
    print("b:", b)  # Output: [1, 2, 3, 4]

if __name__ == "__main__":
    demonstrate_copying_pitfall()