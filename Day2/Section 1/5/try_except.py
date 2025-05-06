# try/except: Catch division by zero and print "Cannot divide".

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")