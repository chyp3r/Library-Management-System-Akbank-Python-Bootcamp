from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import QWidget,QDialog
from ui.mainwindow import Ui_MainWindow
from ui.addbookwidget import Ui_Form as addbook
from ui.removebookwidget import Ui_Form as removebook
from ui.listwidget import Ui_Form as listbook 
from ui.info import Ui_Dialog as info

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.listbutton.clicked.connect(lib.show_list)
        self.addbutton.clicked.connect(lib.show_add)
        self.removebutton.clicked.connect(lib.show_remove)
        self.pushButton.clicked.connect(QtWidgets.QApplication.instance().quit)

class AddBookWidget(QWidget,addbook):
    def __init__(self, *args, obj=None, **kwargs):
        super(AddBookWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addButton.clicked.connect(lib.add_book)

class RemoveBookWidget(QWidget,removebook):
    def __init__(self, *args, obj=None, **kwargs):
        super(RemoveBookWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.removeButton.clicked.connect(lib.remove_book)

class ListBookWidget(QWidget,listbook):
    def __init__(self, *args, obj=None, **kwargs):
        super(ListBookWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)

class InfoWidget(QDialog,info):
    def __init__(self, *args, obj=None, **kwargs):
        super(InfoWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)



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

    def show_list(self):
        self.l = ListBookWidget()
        self.list_book()
        self.l.show()

    def show_add(self):
        self.a = AddBookWidget()
        self.a.show()

    def show_remove(self):
        self.r = RemoveBookWidget()
        self.r.show()

    def show_info(self,text = "Error"):
        self.i = InfoWidget()
        _translate = QtCore.QCoreApplication.translate
        self.i.infolabel.setText(_translate("Dialog", text))
        self.i.show()

    def list_book(self):    
        self.read_book()
        for item in self.books:
            temp = item.split(",")
            self.l.booklist.addItem(f"{temp[0]} -> {temp[1]}")

    def add_book(self):
        self.read_book()
        line = ""
        if self.books != []:
            line+="\n"
        if  self.a.booktitle.text() and self.a.author.text() and self.a.release.text() and self.a.pagecount.text():
            line  +=self.a.booktitle.text()+","+self.a.author.text()+","+self.a.release.text()+","+self.a.pagecount.text()
            self.file.write(line)
            self.a.close()
        else:
            self.show_info(text = "All data must be entered.")

    def remove_book(self):
        self.read_book()
        title = self.r.removetitle.text()
        for item in self.books:
            temp = item.split(",")
            if (temp[0] == title):
                print("A book to be deleted was found")
                self.books.pop(self.books.index(item))
                self.delete_book_data()
                self.file.writelines(self.books)
                self.r.close()
                self.show_info(text = "The book you are looking for has been deleted")
                break
            else:
                self.show_info(text = "The book you were looking for was not found")
                
lib = library()
