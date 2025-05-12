import pickle

class Person:
    def __init__(self, name, educational_institution, colleagues):
        self.name = name
        self.educational_institution = educational_institution
        self.colleagues = colleagues
        
    def __repr__(self):
        return (f"Person(name={self.name}, "
                f"educational_institutions={self.educational_institution}, "
                f"colleagues={self.colleagues})")


pickle_file = "person.pkl"
with open(pickle_file, "rb") as file:
    deserialized_person = pickle.load(file)

print("Deserialized Person object:")
print(deserialized_person)
