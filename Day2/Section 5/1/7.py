from collections import defaultdict

d = defaultdict(lambda: "N/A")
d["key1"] = "value1"

print(d["key1"])
print(d["key2"])
