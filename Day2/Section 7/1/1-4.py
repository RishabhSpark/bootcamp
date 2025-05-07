@profile
def my_function():
    result = sum(x*x for x in range(1000000))
    return result
