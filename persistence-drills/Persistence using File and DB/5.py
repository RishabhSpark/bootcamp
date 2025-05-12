import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def to_dict(self):
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year
        }

    def save_to_yaml(self, filename):
        with open(filename, 'w') as file:
            yaml.dump(self.to_dict(), file)

pagani_huayra = Car(
    make="Pagani",
    model="Huayra Roadster BC",
    year=2021
)

pagani_huayra.save_to_yaml("car.yaml")

print("Car saved to car.yaml")