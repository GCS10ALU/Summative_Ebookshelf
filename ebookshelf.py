import mysql.connector

class Book:
    def __init__(self, title, author, content, rating=None, category=None, year_published=None):
        self.title = title
        self.author = author
        self.content = content
        self.rating = rating
        self.category = category
        self.year_published = year_published

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
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), content TEXT, rating INT, category VARCHAR(255), year_published INT)")

    def add_book(self, book):
        sql = "INSERT INTO books (title, author, content, rating, category, year_published) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (book.title, book.author, book.content, book.rating, book.category, book.year_published)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def load_books(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return [Book(row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]

    def display_books(self):
        books = self.load_books()
        if books:
            for i, book in enumerate(books, start=1):
                print(f"\n {i}. {book.title} by {book.author}")
        else:
            print("No books in the library.")

    def search_book(self, query):
        sql = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
        values = (f"%{query}%", f"%{query}%")
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        return [Book(row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]

    def filter_books(self, genre, year):
        sql = "SELECT * FROM books WHERE category = %s AND year_published = %s"
        values = (genre, year)
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        return [Book(row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]


class SchoolLibrarySystem:
    def __init__(self):
        self.library = Library()
        self.books_searched = 0
        self.books_read = 0
        self.books_recorded = 0

    def welcome_screen(self):
        print("\033[1;36m")  # Set text color to cyan
        print("*" * 40)
        print("*" + " " * 38 + "*")
        print("*" + " " * 8 + "\033[1;33mWelcome to EbookShelf\033[1;36m" + " " * 9 + "*")
        print("*" + " " * 38 + "*")
        print("*" * 40)
        print("\033[0m")

    def start(self):
        self.welcome_screen()
        print("You have the following options:")
        while True:
            print("\033[1;32m") 
            print("1. Read a book")
            print("2. Record a book")
            print("3. Search for a book")
            print("4. Filter books by genre and year published")
            print("5. Show your statistics")
            print("6. Exit")
            print("\033[0m")
            choice = input("Enter the number corresponding to your choice: ")
            if choice == "1":
                self.read_book()
            elif choice == "2":
                self.record_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.filter_books()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                print("Thank you for using the School Library System. Goodbye!")
                break
            else:
                print("\033[1;31m") 
                print("Invalid choice. Please enter a valid option.")
                print("\033[0m") 

    def read_book(self):
        print("\033[1;32m") 
        print("\nList of available books:")
        print("\033[0m")
        self.library.display_books()
        choice = input("\n \033[1;33mEnter the number of the book you want to read: \033[0m")
        try:
            index = int(choice) - 1
            selected_book = self.library.load_books()[index]
            print("\033[1;32m") 
            print("\nReading book:", selected_book.title)
            print("\033[0m")
            print(selected_book.content)
            self.books_read += 1  # Increment books read count
            while True:
                option = input("\nContinue reading? (Y/N): ")
                if option.upper() == "Y":
                    break
                elif option.upper() == "N":
                    return
                else:
                    print("\033[0m") 
                    print("Invalid input. Please enter Y or N ")
                    print("\033[0m")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")

    def record_book(self):
        print("\nRecording a new book:")
        title = input("\033[1;33mEnter the name of the book: \033[0m")
        author = input("\033[1;33mEnter the name of the author: \033[0m")
        content = input("\033[1;33mEnter the content of the book: \033[0m")
        rating = input("\033[1;33mEnter the rating (1-5): \033[0m")
        category = input("\033[1;33mEnter the genre of the book: \033[0m")
        year_published = input("\033[1;33mEnter the year published: \033[0m")
        new_book = Book(title, author, content, rating, category, year_published)
        self.library.add_book(new_book)
        self.books_recorded += 1  # Increment books recorded count
        print("\nBook recorded successfully.")

    def search_book(self):
        query = input("\n \033[1;33mEnter the title or author of the book you want to search: \033[0m")
        results = self.library.search_book(query)
        if results:
            print("\nSearch results:")
            for i, book in enumerate(results, start=1):
                print(f"{i}. {book.title} by {book.author}")
            self.books_searched += len(results)  # Increment books searched count
        else:
            print("\nNo matching books found.")

    def filter_books(self):
        genre = input("\n\033[1;33mEnter the genre of the books you want to filter: \033[0m")
        year = input("\033[1;33mEnter the year of publication for the books you want to filter: \033[0m")
        filtered_books = self.library.filter_books(genre, year)
        if filtered_books:
            print("\n\033[1;32mFiltered books:\033[0m")
            for i, book in enumerate(filtered_books, start=1):
                print(f"\n{i}. {book.title} by {book.author}")
        else:
            print("\nNo books found for the specified filters.")

    def show_statistics(self):
        print("\nYour Statistics:")
        print(f"\033[1;33mBooks searched: \033[0m{self.books_searched}")
        print(f"\033[1;33mBooks read: \033[0m{self.books_read}")
        print(f"\033[1;33mBooks recorded: \033[0m{self.books_recorded}")


# Main program
if __name__ == "__main__":
    school_library_system = SchoolLibrarySystem()
    school_library_system.start()
