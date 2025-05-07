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
        return f"[Book] {self.title} by {self.author}"


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: {super().describe()} - Genre: {self.genre}"


class AudioMixin:
    def play_audio_sample(self):
        return f"Playing audio sample of '{self.title}'"


class AudioBook(AudioMixin, Book):
    def __init__(self, title, author, duration_minutes):
        super().__init__(title, author)
        self.duration = duration_minutes


# Test Novel subclass
novel = Novel("Dune", "Frank Herbert", "Science Fiction")
print(novel.describe())
print(isinstance(novel, Book))  # True

# Test __str__ override in Book
print(novel)  # Uses __str__ from Book

# Test AudioBook with multiple inheritance
audiobook = AudioBook("Sapiens", "Yuval Noah Harari", 720)
print(audiobook.describe())
print(audiobook.play_audio_sample())

# Polymorphism in action
books = [Book("The Hobbit", "Tolkien"), novel, audiobook]
for b in books:
    print(b.describe())