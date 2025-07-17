books = [
    {"id": "1", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "available"},
    {"id": "2", "title": "1984", "author": "George Orwell", "status": "available"},
    {"id": "3", "title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "lent"},
]

def lend_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "available":
                book["status"] = "lent"
                print(f"Book '{book['title']}' has been lent out.")
                return
            else:
                print(f"Book '{book['title']}' is already lent.")
                return
    print("Book ID not found.")

def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "lent":
                book["status"] = "available"
                print(f"Book '{book['title']}' has been returned.")
                return
            else:
                print(f"Book '{book['title']}' was not lent.")
                return
    print("Book ID not found.")