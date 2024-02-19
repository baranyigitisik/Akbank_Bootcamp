class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            print("List of books:")
            for book in books:
                title, author, release_date, num_pages = book.split(',')
                print(f"Title: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        found = False
        updated_books = []
        for book in books:
            book_info = book.split(',')
            if title == book_info[0]:
                found = True
            else:
                updated_books.append(book)
        if not found:
            print(f"Book '{title}' not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book + '\n')
            print(f"Book '{title}' removed successfully.")


lib = Library()


while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        del lib  
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
