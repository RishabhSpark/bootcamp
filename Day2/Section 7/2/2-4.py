big_list = [x for x in range(1000000)]

# Check if any number is divisible by 99
result = any(x % 99 == 0 for x in big_list)
print(f"Is any number divisible by 99? {result}")
