from typing import Mapping


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        pass


    # Available Books
    def displayAvailableBooks(self):
        print("The available books are: ")
    
        for i, book in enumerate(self.books):
            print(f'{i+1}.{book}')

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f'Congratulations! You have issued the {bookname} Happy Reading!')
            self.books.remove(bookname)
        else:
            print("Sorry! This book is already issued by someone else or the book is not available")

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this book")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to Return or Add: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["C", "C++", "Python", "JAVA", "HTML", "CSS"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = '''==== WELCOME====
        Choose an option:
        1. List all the books
        2. Request a Book
        3. Return a Book or Add new book
        4. Exit'''

        print(welcomeMsg)


        a = int(input("Enter your choice: "))
        print('-----------------------------------------------------')
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowbook(student.requestBook())
        elif a == 3:
            centralLibrary.returnbook(student.returnBook())
        elif a == 4:
            print("Thank you Visit Again!")
            exit()
        else:
            print("You have entered wrong choice")
        



