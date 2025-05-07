# Use cycle to Repeat a Pattern: Cycle through ["red", "green", "blue"] and print 6 items.

import itertools

color_list = ["red", "green", "blue"]

repeat_pattern = itertools.cycle(color_list)

for _ in range(6):
    print(next(repeat_pattern))