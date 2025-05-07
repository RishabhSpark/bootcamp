import itertools

items = [
    {'name': 'apple', 'category': 'fruit'},
    {'name': 'banana', 'category': 'fruit'},
    {'name': 'carrot', 'category': 'vegetable'},
    {'name': 'potato', 'category': 'vegetable'}
]

grouped = itertools.groupby(items, key=lambda x: x['category'])

for key, group in grouped:
    print(key)
    for item in group:
        print(item)
