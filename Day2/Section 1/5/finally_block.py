# finally Block: Use finally to print "Cleanup done" no matter what happens.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Tried division")