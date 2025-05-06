# try/except/else: Attempt division, print "Success" only if no exception.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Success")