from collections import defaultdict

# Build a defaultdict of defaultdict(int) for hierarchical data
d = defaultdict(lambda: defaultdict(int))

d["category1"]["item1"] += 1
d["category1"]["item2"] += 2
d["category2"]["item3"] += 3

# Access the data
print(d["category1"])
print(d["category2"])

# Access a non-existent category, which will return a defaultdict(int)
print(d["category3"])
