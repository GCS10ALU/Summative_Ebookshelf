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

    def save_books(self):
        with open(self.filename, "a") as file:  # Use "a" for append mode
            for book in self.books[-1:]:  # Save only the last added book
                file.write(str(book) + "\n")

    def display_books(self):
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book.title} by {book.author}")

    def search_book(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results

    def get_book(self, index):
        return self.books[index]
