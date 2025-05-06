def make_multiplier(n: int):
    """
    Returns a function that multiplies its input by 'n'.
    
    Args:
        n (int): The multiplier.
    
    Returns:
        function: A function that multiplies its input by 'n'.
    """
    def multiplier(x: int) -> int:
        return x * n
    
    return multiplier

triple = make_multiplier(3)
print(triple(10))