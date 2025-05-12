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
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            genres=data['genres']
        )
            
loaded_book = Book.from_file("book.json")

print("Deserialized from file:")
print(f"Title: {loaded_book.title}")
print(f"Author: {loaded_book.author}")
print(f"Year: {loaded_book.year}")
print(f"Genres: {loaded_book.genres}")
