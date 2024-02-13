import library

lib = library.library()

while True:
    print("""
    *** MENU*** 
1) List Books 
2) Add Book 
3) Remove Book
4) UI Mode 
Q) Quit
""")
    value = input("Give: ")
    if value == "1":
        lib.list_book()
    elif value == "2":
        lib.add_book()
    elif value == "3":
        lib.remove_book()
    elif value == "4":
        #UI MODE HERE
        pass
    elif value.lower() == "q":
        break
    else:
        print("Hebele")