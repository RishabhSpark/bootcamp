# data = pickle.load(some_untrusted_source)

# Safer alternatives:
import json

# Use json for safe serialization/deserialization
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
loaded_data = json.loads(json_string)
print(f"Loaded data using json: {loaded_data}")
