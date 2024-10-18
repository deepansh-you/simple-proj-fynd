from crud import add_book, get_book, add_member, get_member, issue_book, return_book, get_transactions_by_member

def addNewBook():
    title = input("Enter title : ")
    author = input("Enter author's name : ")
    isbn = input("Enter ISBN : ")
    count = int(input("Enter number of copies : "))
    add_book(title, author, isbn, count)
    

def printBooks():
    books = get_book()
    for book in books:
        available = "Available" if book.count > 0 else "Not Available"
        print(f"{book.id} : '{book.title}' by {book.author} (ISBN : {book.isbn}) {available} ({book.count} copies)")


def addNewMember():
    name = input("Enter Member Name : ")
    email = input("Enter Member Email : ")
    add_member(name, email)
    
def printMembers():
    members = get_member()
    for member in members:
        print(f"{member.id} {member.name} {member.email}")
        
def issueABook():
    book_id = int(input("Enter Book ID : "))
    member_id = int(input("Enter Member ID : "))
    issue_book(book_id, member_id)
    
def returnBook():
    transaction_id = int(input("Enter a transaction ID : "))
    return_book(transaction_id)
    
def getTransactionForMember():
    member_id = int(input("Enter member ID : "))
    transactions = get_transactions_by_member(member_id)
    for transaction in transactions:
        return_status = "Returned" if transaction.return_date else "Not Returned"
        print(f"Transaction ID : {transaction.id}, Book ID : {transaction.book_id}, Issue Date : {transaction.issue_date}, Return Date : {transaction.return_date}, Status : {return_status} ")
    
def main():
    while True:
        print("****************\n")
        print("1. Add Book")
        print("2. View Book")
        print("3. Add Member")
        print("4. View Member")
        print("5. Issue Book ")
        print("6. Return Book")
        print("7. View Transactions by Member")
        print("8. Exit\n")
        print("****************")
        choice = input("Enter your choice : ")
        
        if choice == "1":
            addNewBook()
        elif choice == "2":
            printBooks()
        elif choice == "3":
            addNewMember()
        elif choice == "4":
            printMembers()
        elif choice == "5":
            issueABook()
        elif choice == "6":
            returnBook()
        elif choice == "7":
            getTransactionForMember()
        else:
            break
    
if __name__=="__main__":
    main()