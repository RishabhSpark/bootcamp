import json

class Book:
    def __init__(self, title, author, year, genres):
        self.title = title
        self.author = author
        self.year = year
        self.genres = genres

    def to_json(self):
        return json.dumps({
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genres': self.genres
        }, indent=4)
        
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.to_json())

book = Book(
    title="Mistborn: The Final Empire",
    author="Brandon Sanderson",
    year=2006,
    genres=["Fantasy", "Epic", "Magic"]
)

book.save_to_file("book.json")

book_json = book.to_json()

print("Book as JSON:")
print(book_json)
