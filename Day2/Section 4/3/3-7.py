from functools import partial
from collections import defaultdict

default_dict = partial(defaultdict, dict)

nested_dict = default_dict()
nested_dict["key1"]["subkey"] = "value"
print(nested_dict)