
#-------------------------------
#    simple library management.
#-------------------------------

class book:
    def __init__(self , title):
        self.title=title
        self.is_available=True       # its show book availabilty

    def __str__(self):
        status="Available" if self.is_available else "Not Available"
        return f"{self.title} is {status}"
    
class library:
    def __init__(self):
        self.Book=[ ]

    def Add_book(self, title):
        # Add book to library
        new_book=book(title)
        self.Book.append(new_book)
        print(f"book Added= {title}")

    def show_book(self):
        #display all Available book..
        print("Available Books")
        Book_found=False
        for book in self.Book:
            if book.is_available:
                print(f"- {book.title}")
                Book_found=True
        if not Book_found:
            print("No books available right now.")

    def borrow_book(self, title):
        # borrow book if  available
        for book in self.Book:
            if book.title==title and book.is_available:
                book.is_available=False
                print(f"you borrowed : '{title}'")
                return
        print(f"sorry! {title} book is not available.")

    def return_book(self, title):
        # returned the borrow book
        for book in self.Book:
            if book.title==title and not book.is_available:
                book.is_available=True
                print(f"you returned -{title}")
                return
        print(f"you dont have the book {title}")



#------ testing the system-----------

obj=library()
obj.Add_book("physics")
obj.Add_book("maths")
obj.Add_book("computer science")
obj.Add_book("python")

obj.show_book()

obj.borrow_book("python")

obj.return_book("")

obj.show_book()




                


            


            
        