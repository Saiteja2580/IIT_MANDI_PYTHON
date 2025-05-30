class Member:
    def __init__(self,name,id):
        self.name = name
        self.membership_id = id


class StudentMember(Member):
    def __init__(self,name,id):
        super().__init__(name,id)
        self.books = 0

    def add_book(self):
        self.books+=1
        print("book is added")

    def return_book(self):
        if self.books>0:
            self.books-=1
            print(f"Returned The book & No.of books to return : {self.books}")
        else:
            print("There are no books to return")


library = StudentMember("Sai Teja","123")
library.add_book()
library.add_book()
library.return_book()