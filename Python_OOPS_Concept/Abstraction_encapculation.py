class Library:
    def __init__(self,listOfBooks):
        self.avaiableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Avaialble Books: ")

        for books in self.avaiableBooks:
            print(books)


    def lendBook(self, requestedBook):
        if requestedBook in self.avaiableBooks:
            print("You have now borrowed the book")
            self.avaiableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our list")

    def addBook(self, returnedbook):
        self.avaiableBooks.append(returnedbook)
        print("You have returned the book. Thank you!")


class Customer:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to lend: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

libr = Library(["Python", "Java", "C++"])
cust = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice == 1:
        libr.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = cust.requestBook()
        libr.lendBook(requestedBook)
    elif userChoice == 3:
        returnBook = cust.returnBook()
        libr.addBook(returnBook)
    elif userChoice == 4:
        quit()
