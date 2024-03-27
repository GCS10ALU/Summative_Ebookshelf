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
 def load_books(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 4):
                    title = lines[i].strip()
                    author = lines[i+1].strip()[4:]  # Remove "By: " prefix
                    content = lines[i+3].strip()
                    self.books.append(Book(title, author, content))
        except FileNotFoundError:
            print("No library file found. Starting with an empty library.")

