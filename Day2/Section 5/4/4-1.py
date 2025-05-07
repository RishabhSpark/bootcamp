import json

# Serialize a Python dict to a JSON string
data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

# Deserialize JSON string back to Python dict
loaded_data = json.loads(json_string)
print(f"Loaded data: {loaded_data}")