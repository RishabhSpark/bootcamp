from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("OrderedDict items:")
for key, value in od.items():
    print(f"{key}: {value}")
