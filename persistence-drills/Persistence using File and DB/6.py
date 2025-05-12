import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def from_dict(cls, data):
        return cls(
            make=data['make'],
            model=data['model'],
            year=data['year']
        )

    @classmethod
    def load_from_yaml(cls, filename):
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        return cls.from_dict(data)
    

pagani_huayra = Car.load_from_yaml("car.yaml")
print('Loaded car from YAML:')
print(f"Make: {pagani_huayra.make}")
print(f"Model: {pagani_huayra.model}")
print(f"Year: {pagani_huayra.year}")