# 5. Static and Class Methods¶
# Static Method: Add a @staticmethod that validates if a string is a valid ISBN.
# Class Method: Add a @classmethod from_string(cls, s) to parse "Title|Author" into a Book.
# Use cls in Class Method: Return cls(...) from the class method and verify it works with subclass too.
# Difference in Behavior: Show that static methods don’t get access to cls or self.
# Alternative Constructor: Create multiple factory-style @classmethods for Book, e.g., from JSON or dict.
# Invoke Static Method: Call static method from both class and instance.
# Method Resolution: Show what happens when a class method is overridden in a subclass.
# Hybrid Method Example: Discuss a situation where static, class, and instance methods might all be used in the same class.


from dataclasses import dataclass
import json

@dataclass
class Book:
    title: str
    author: str

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        return isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13)

    @classmethod
    def from_string(cls, s: str):
        title, author = s.split("|")
        return cls(title.strip(), author.strip())

    @classmethod
    def from_dict(cls, data: dict):
        return cls(title=data.get("title", ""), author=data.get("author", ""))

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls.from_dict(data)

    def describe(self):
        return f"Book: '{self.title}' by {self.author}"

class Novel(Book):
    def describe(self):
        return f"Novel: '{self.title}' by {self.author}"

    @classmethod
    def from_string(cls, s: str):
        print("Called from Novel")
        return super().from_string(s)

# Testing
print(Book.is_valid_isbn("1234567890"))
print(Book.is_valid_isbn("abc"))

b1 = Book.from_string("1984 | Orwell")
b2 = Book.from_dict({"title": "Animal Farm", "author": "Orwell"})
b3 = Book.from_json('{"title": "Brave New World", "author": "Huxley"}')

print(b1.describe())
print(b2.describe())
print(b3.describe())

n1 = Novel.from_string("Dune | Herbert")
print(n1.describe())

# Static method from instance and class
print(b1.is_valid_isbn("0123456789123"))
print(Book.is_valid_isbn("abc"))

# Method resolution demo
print(isinstance(n1, Book))