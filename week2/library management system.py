class Book:
    def __init__(self, Book_id, Book_Title, Author_Name):
        self.Book_id = Book_id
        self.Book_Title = Book_Title
        self.Author_Name = Author_Name
        self.Availability_Status = True

    def get_data(self):
        print("\nBook_id =", self.Book_id)
        print("Book_Title =", self.Book_Title)
        print("Author_Name =", self.Author_Name)
        print("Availability_Status =", self.Availability_Status)
        if self.Availability_Status:
            print("Book is Available")
        else:
            print("Book is not available")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        Book_id = int(input("Enter Book_id: "))

        if Book_id in self.books:
            print("Book ID already exists!")
        else:
            Book_Title = input("Enter Title: ")
            Author_Name = input("Enter Author: ")

            new_book = Book(Book_id, Book_Title, Author_Name)
            self.books[Book_id] = new_book
            print("Book Added Successfully")

    def view_book(self):
        if not self.books:
            print("No Books Available")
        else:
            for book in self.books.values():
                book.get_data()

    def issue_book(self):
        book_id = int(input("Enter Book ID: "))

        if book_id in self.books:
            book = self.books[book_id]

            if book.Availability_Status == False:
                print("Book is already Issued")
            else:
                book.Availability_Status = False
                print("Book Issued Successfully")
        else:
            print("Book Not Found")

    def return_book(self):
        book_id = int(input("Enter Book ID: "))

        if book_id in self.books:
            book = self.books[book_id]

            if book.Availability_Status:
                print("Book Was Not Issued")
            else:
                book.Availability_Status = True
                print("Book Returned Successfully")
        else:
            print("Book Not Found")

    def search_book(self):
        Book_id=int(input("Enter book_id:"))
        if Book_id in self.books:
            self.books[Book_id].get_data()
        else:
            print("Book not found")    
            


l1 = Library()

while True:
    print("\n---------------------- OPTIONS ----------------------")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = int(input("Enter choice (1-5): "))

    if choice == 1:
        l1.add_book()

    elif choice == 2:
        l1.view_book()

    elif choice == 3:
        l1.issue_book()

    elif choice == 4:
        l1.return_book()

    elif choice == 5:
        l1.search_book()    

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")