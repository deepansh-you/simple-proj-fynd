from models import Book
from database import session

def add_book(title, author, isbn, count):
    print("Adding Book...")
    book=Book(title = title, author = author, isbn = isbn, count = count)
    session.add(book)
    session.commit()