import pickle

class Person:
    def __init__(self, name):
        self.name = name
        self.friend = None
        
    def __repr__(self):
        return f"Person(name={self.name}, friend={self.friend.name if self.friend else None})"
                
Rishabh = Person("Rishabh")
Ishaan = Person("Ishaan")

Ishaan.friend = Rishabh
Rishabh.friend = Ishaan

with open("cyclic.pkl", "wb") as f:
    pickle.dump(Rishabh, f)
    
with open("cyclic.pkl", "rb") as f:
    loaded_rishabh = pickle.load(f)

print("Loaded Person:", loaded_rishabh)
print("Friend of loaded person:", loaded_rishabh.friend)
print("Back-reference (cyclic):", loaded_rishabh.friend.friend is loaded_rishabh)