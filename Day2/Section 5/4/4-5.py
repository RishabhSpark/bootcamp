import pickle

data = {"name": "Alice", "age": 30, "city": "New York"}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(f"Loaded data: {loaded_data}")
