import json

data = {"name": "Alice", "age": 30, "city": "New York"}
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(f"Pretty JSON:\n{pretty_json}")
