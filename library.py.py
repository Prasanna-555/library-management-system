class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book}" added to the library.')

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available Books:")
            for book in self.books:
                print(f" - {book}")

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You have borrowed "{book}".')
        else:
            print(f'Sorry, "{book}" is not available.')

    def return_book(self, book):
        self.books.append(book)
        print(f'Thank you for returning "{book}".')
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book):
        if book in library.books:
            library.borrow_book(book)
            self.borrowed_books.append(book)
        else:
            print(f'Sorry, "{book}" is not available.')

    def return_book(self, library, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.return_book(book)
        else:
            print(f'You do not have "{book}" to return.')
def main():
    library = Library()
    user = User("Alice")  # Example user

    while True:
        print("\n📚 Library Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book = input("Enter book name: ")
            library.add_book(book)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book = input("Enter book name to borrow: ")
            user.borrow_book(library, book)

        elif choice == "4":
            book = input("Enter book name to return: ")
            user.return_book(library, book)

        elif choice == "5":
            print("Exiting the Library System. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
