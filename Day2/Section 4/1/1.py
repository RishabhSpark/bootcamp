def apply(func, value):
    return func(value)

if __name__ == "__main__":
    print(apply(str.upper, "hello"))