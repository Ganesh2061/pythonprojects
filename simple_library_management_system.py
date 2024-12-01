class library:
    def __init__(self):
        self.Books=[]
    def addbook(self,name,author):
        Book_info={"name":name,"author":author}
        self.Books.append(Book_info)
    
    def countandcheck(self,no_of_book):
        count=len(self.Books)
        if (count==no_of_book):
            print(f"No.of books are {count}")
        else:
            print("count of book are mismatch")
    
    def showbooks(self):
        if not self.Books:
            print("No books in libarary")
        else:
            print("The books are in library are")
            for index, book in enumerate(self.Books,start=1):
                print(f"{index}.\t {book['name']}\t {book['author']}")

a=library()
a.addbook("Think and grow reach","Nepoleanhill")
a.addbook("Zero To One","Peter Thrill")
a.countandcheck(2)
a.showbooks()

    
    

    
