class library():
    def __init__(self):
        try:
            self.file = open("books.txt","+r")
            self.read_book()
        except FileNotFoundError as _:
            self.file = open("books.txt","+w")
            self.read_book()
        except:
            print("An unexpected error occurred")

    def __del__(self):
        self.file.close()
        print("Library deleted successfully") 
    
    def delete_book_data(self):
        try:
            self.file = open("books.txt","w")
            self.file.close()
            self.file = open("books.txt","+r")
        except Exception as er:
            print(er)

    def read_book(self):
        self.file.seek(0)
        self.books = self.file.readlines()
    
    def is_booklist_empty(self):
        return self.books == []

    def list_book(self):
        for item in self.books:
            temp = item.split(",")
            print(temp[0],temp[1])

    def add_book(self):
        qs = ["book title","book author","first release year","number of pages"]
        line = ""
        if not self.is_booklist_empty():
            line += "\n"
        for item in qs:
            temp = input(f"Give {item}: ")
            temp += ","
            line += temp
        self.file.seek(0,2)
        self.file.write(f"{line[0:-1]}")

    def remove_book(self):
        title = input("Give title: ")
        for item in self.books:
            temp = item.split(",")
            if (temp[0] == title):
                print("A book to be deleted was found")
                self.books.pop(self.books.index(item))
                self.delete_book_data()
                self.file.writelines(self.books)
                break
                

