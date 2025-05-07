class Book:
    category = "Fiction"

    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

    def update_title(self, new_title):
        self.title = new_title

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __lt__(self, other):
        return self.title < other.title


class Library:
    def __init__(self, books=None):
        self.books = books if books else []

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]


class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"


class CustomFlag:
    def __init__(self, active):
        self.active = active

    def __bool__(self):
        return self.active


# Usage examples
b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
b3 = Book("Animal Farm", "Orwell")

print(str(b1))         # __str__
print(repr(b1))        # __repr__
print(b1 == b2)        # __eq__
print(len(set([b1, b2, b3])))  # __hash__
print(sorted([b3, b1]))        # __lt__

library = Library([b1, b3])
print(len(library))    # __len__
print(library[1])      # __getitem__

greet = Greeter("Rishabh")
print(greet())         # __call__

flag = CustomFlag(False)
if flag:
    print("Flag is active.")
else:
    print("Flag is inactive.")  # __bool__