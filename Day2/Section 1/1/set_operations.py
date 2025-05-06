# Set Operations: From sets a = {1, 2, 3} and b = {3, 4}, print intersection, union, and difference.

def set_operations(a: set, b: set) -> None:
    """
    Performs set operations: intersection, union, and difference on two sets.
    
    Args:
        a (set): First set.
        b (set): Second set.
    """
    intersection = a & b  # or a.intersection(b)
    union = a | b  # or a.union(b)
    difference = a - b  # or a.difference(b)

    print(f"Intersection: {intersection}")
    print(f"Union: {union}")
    print(f"Difference (a - b): {difference}")


if __name__ == "__main__":
    a = {1, 2, 3}
    b = {3, 4}
    set_operations(a, b)