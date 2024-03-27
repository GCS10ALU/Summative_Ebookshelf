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
    
     def read_book(self):
        print("\nList of available books:")
        self.library.display_books()
        choice = input("\nEnter the number of the book you want to read: ")
        try:
            index = int(choice) - 1
            selected_book = self.library.get_book(index)
            print("\nReading book:", selected_book.title)
            print(selected_book.content)
            while True:
                option = input("\nContinue reading? (Y/N): ")
                if option.upper() == "Y":
                    break
                elif option.upper() == "N":
                    return
                else:
                    print("Invalid input. Please enter Y or N.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")

    def record_book(self):
        print("\nRecording a new book:")
        title = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        content = input("Enter the content of the book: ")
        new_book = Book(title, author, content)
        self.library.add_book(new_book)
        print("\nBook recorded successfully.")

    def search_book(self):
        query = input("\nEnter the title or author of the book you want to search: ")
        results = self.library.search_book(query)
        if results:
            print("\nSearch results:")
            for i, book in enumerate(results, start=1):
                print(f"{i}. {book.title} by {book.author}")
        else:
            print("\nNo matching books found.")


# Main program
if __name__ == "__main__":
    school_library_system = SchoolLibrarySystem()
    school_library_system.start()
