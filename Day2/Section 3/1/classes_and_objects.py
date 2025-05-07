class Book:
    category = "Fiction"

    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

    def update_title(self, new_title):
        self.title = new_title


book1 = Book("1984", "Orwell")
print(book1.title, book1.author)

print(book1.describe())

print(book1.category)

book1.update_title("Nineteen Eighty-Four")
print(book1.describe())

book2 = Book()
print(book2.describe())

book1.year = 1949
print(book1.year)

print(isinstance(book1, Book))