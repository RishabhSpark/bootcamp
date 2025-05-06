def calculate_area(radius: float, /) -> float:
    """
    Calculates the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle. This argument is positional-only.
    
    Returns:
        float: The area of the circle.
    """
    return 3.14 * radius ** 2

if __name__ == "__main__":
    print(calculate_area(5))