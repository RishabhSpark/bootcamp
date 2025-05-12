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

person_instance = Person(
    name="Rishabh",
    educational_institution = ["Bennett University", "National Taiwan University"],
    colleagues = ["Ishaan", "Siddharth"]
)

pickle_path = "person.pkl"
with open(pickle_path, "wb") as file:
    pickle.dump(person_instance, file)

print(f"Person object serialized successfully to {pickle_path}")