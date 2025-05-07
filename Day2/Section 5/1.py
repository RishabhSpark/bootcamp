from collections import defaultdict

fruits = ['apple', 'banana', 'blueberry', 'cherry']
grouped_by_first_letter = defaultdict(list)

for fruit in fruits:
    grouped_by_first_letter[fruit[0]].append(fruit)

print(grouped_by_first_letter)