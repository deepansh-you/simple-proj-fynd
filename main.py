from crud import add_book

def main():
    print("****************\n")
    print("1. Add Book")
    print("2. View Book\n")
    print("****************")
    choice = input("Enter your choice : ")
    
    if choice == "1":
        title = input("Enter title : ")
        author = input("Enter author's name : ")
        isbn = input("Enter ISBN : ")
        count = int(input("Enter number of copies : "))
        add_book(title, author, isbn, count)
    elif choice == "2":
        print("Write code to view book")
    
if __name__=="__main__":
    main()