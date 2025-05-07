from functools import partial

custom_print = partial(print, end=" - ")

custom_print2 = partial(custom_print, sep="|")

custom_print2("Hello", "World")