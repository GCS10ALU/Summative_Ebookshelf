class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return f"{self.title}\nBy: {self.author}\n\n{self.content}\n"


class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

