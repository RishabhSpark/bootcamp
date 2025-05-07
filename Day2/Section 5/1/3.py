from collections import Counter

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 3, 4, 6, 8, 2, 4]

print(Counter(lst).most_common(2))
