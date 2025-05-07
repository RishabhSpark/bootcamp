try:
    result = 1 / 0
except Exception as e:
    print(type(e), e)