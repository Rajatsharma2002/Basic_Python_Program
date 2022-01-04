class Library:
    def __init__(self,library_name,*list_of_books):
        self.list_of_books=list(list_of_books)
        self.library_name=library_name
        self.dict={}

    def display_book(self):
        print(f"{self.library_name} contains following books .....")
        print(self.list_of_books)

    def lend_book(self):
        l=input("Enter the book you want to lend : ")
        if l in self.list_of_books:
            print("BOOK FOUND")
            name=input("Enter your name : ")
            self.dict.update({l:name})
            # print(self.dict)
            a=self.list_of_books.index(l)
            self.list_of_books.pop(a)
            print(f"{name} issued {l} Book successfully")
        elif l in self.dict:
            k_v=self.dict.get(l)
            print(f"Book is already issued by {k_v}")
        else:
            print("BOOK not found in LIBRARY")

    def add_book(self):
        b=input("Enter the book you want to add : ")
        self.list_of_books.append(b)
        print(self.list_of_books)

    def return_book(self):
        r=input("enter the name of book you want to return : ")
        self.list_of_books.append(r)
        self.dict.pop(r)
        print(f"{r} book returned successfully")
        print(self.list_of_books)

    def issue(self):
        print(f"Books issued till now : \n{self.dict}")

if __name__ == '__main__':
    raj_library=Library("Raj_library","python","c++ bigenner","Ai handbook","IBM intro to ML")
    while(True):
        choice=int(input("\nEnter the function you want to execute in the library \n1.Display books\n2.Lend book\n"
                         "3.Add book\n4.Return book\n5.BOOKS ISSUED TILL NOW\n0.exit\n"))
        if choice==0:
            print("LIBRARY IS CLOSED")
            break
        elif choice ==1:
            raj_library.display_book()
        elif choice==2:
            raj_library.lend_book()
        elif choice==3:
            raj_library.add_book()
        elif choice==4:
            raj_library.return_book()
        elif choice==5:
            raj_library.issue()
        else:
            print( "Invalid choice")





# class Library:
#     def __init__(self, list, name):
#         self.booksList = list
#         self.name = name
#         self.lendDict = {}
#
#     def displayBooks(self):
#         print(f"We have following books in our library: {self.name}")
#         for book in self.booksList:
#             print(book)
#
#     def lendBook(self, user, book):
#         if book not in self.lendDict.keys():
#             self.lendDict.update({book:user})
#             print("Lender-Book database has been updated. You can take the book now")
#         else:
#             print(f"Book is already being used by {self.lendDict[book]}")
#
#     def addBook(self, book):
#         self.booksList.append(book)
#         print("Book has been added to the book list")
#
#     def returnBook(self, book):
#         self.lendDict.pop(book)
#
# if __name__ == '__main__':
#     harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")
#
#     while(True):
#         print(f"Welcome to the {harry.name} library. Enter your choice to continue")
#         print("1. Display Books")
#         print("2. Lend a Book")
#         print("3. Add a Book")
#         print("4. Return a Book")
#         user_choice = input()
#         if user_choice not in ['1','2','3','4']:
#             print("Please enter a valid option")
#             continue
#
#         else:
#             user_choice = int(user_choice)
#
#
#         if user_choice == 1:
#             harry.displayBooks()
#
#         elif user_choice == 2:
#             book = input("Enter the name of the book you want to lend:")
#             user = input("Enter your name")
#             harry.lendBook(user, book)
#
#         elif user_choice == 3:
#             book = input("Enter the name of the book you want to add:")
#             harry.addBook(book)
#
#         elif user_choice == 4:
#             book = input("Enter the name of the book you want to return:")
#             harry.returnBook(book)
#
#         else:
#             print("Not a valid option")
#
#
#         print("Press q to quit and c to continue")
#         user_choice2 = ""
#         while(user_choice2!="c" and user_choice2!="q"):
#             user_choice2 = input()
#             if user_choice2 == "q":
#                 exit()
#
#             elif user_choice2 == "c":
#                 continue

