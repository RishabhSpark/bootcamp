def compose(f, g):
    return lambda x: f(g(x))

double = lambda x: x * 2 # f(x)
increment = lambda x: x + 1 # g(x)
composed = compose(double, increment) # f(g(x))
print(composed(10))