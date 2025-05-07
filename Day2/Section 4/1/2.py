def make_doubler():
    return lambda x: x * 2

doubler = make_doubler()
print(doubler(20))