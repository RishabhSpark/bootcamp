# Using return (inefficient for large data)
def generate_squares_return(n):
    result = []
    for x in range(n):
        result.append(x * x)
    return result

# Using yield (efficient for large data)
def generate_squares_yield(n):
    for x in range(n):
        yield x * x

for square in generate_squares_yield(1000000):
    if square > 100:
        print(square)
        break
