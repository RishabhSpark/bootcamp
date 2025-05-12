import json

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_json(self):
        return {
            'name': self.name,
            'price': self.price
        }

    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], price=data['price'])

class MyCollection:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)

    def to_json(self):
        return json.dumps({
            'items': [item.to_json() for item in self.items]
        }, indent=4)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        items = [Item.from_json(item) for item in data['items']]
        return cls(items)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.to_json())

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as file:
            json_data = file.read()
        return cls.from_json(json_data)

    def display(self):
        for item in self.items:
            print(f"Item: {item.name}, Price: {item.price}")
            
            
item1 = Item("Apple", 20)
item2 = Item("PS5", 50000)
item3 = Item("Pen", 10)

collection = MyCollection([item1, item2, item3])

print("Original Collection:")
collection.display()

collection_json = collection.to_json()
print("\nSerialized Collection (JSON):")
print(collection_json)

collection.save_to_file("mycollection.json")

loaded_collection = MyCollection.load_from_file("mycollection.json")
print("\nLoaded Collection from File:")
loaded_collection.display()