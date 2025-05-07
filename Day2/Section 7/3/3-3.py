import traceback

try:
    x = 1 / 0
except Exception as e:
    print("An error occurred:")
    print(traceback.format_exc())
