import mysql.connector

class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return f"{self.title}\nBy: {self.author}\n\n{self.content}\n"


class Library:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password="1251Rama1251@rshafii106",
            database="library_db"
            )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), content TEXT)")

    def add_book(self, book):
        sql = "INSERT INTO books (title, author, content) VALUES (%s, %s, %s)"
        values = (book.title, book.author, book.content)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def load_books(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return [Book(row[1], row[2], row[3]) for row in rows]

    def display_books(self):
        books = self.load_books()
        if books:
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book.title} by {book.author}")
        else:
            print("No books in the library.")

    def search_book(self, query):
        sql = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
        values = (f"%{query}%", f"%{query}%")
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        return [Book(row[1], row[2], row[3]) for row in rows]


class SchoolLibrarySystem:
    def __init__(self):
        self.library = Library()

    def start(self):
        print("Welcome to the School Library System!")
        print("You have the following options:")
        while True:
            print("1. Read a book")
            print("2. Record a book")
            print("3. Search for a book")
            print("4. Exit")
            choice = input("Enter the number corresponding to your choice: ")
            if choice == "1":
                self.read_book()
            elif choice == "2":
                self.record_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                print("Thank you for using the School Library System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def read_book(self):
        print("\nList of available books:")
        self.library.display_books()
        choice = input("\nEnter the number of the book you want to read: ")
        try:
            index = int(choice) - 1
            selected_book = self.library.load_books()[index]
            print("\nReading book:", selected_book.title)
            print(selected_book.content)
            while True:
                option = input("\nContinue reading? (Y/N): ")
                if option.upper() == "Y":
                    break
                elif option.upper() == "N":
                    return
                else:
                    print("Invalid input. Please enter Y or N ")
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
