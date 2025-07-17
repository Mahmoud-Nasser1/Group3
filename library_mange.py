import json
import os

DB_FILE = "library.json"

# -------------------------------
# Load and Save Functions
# -------------------------------

def load_books():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open(DB_FILE, "w", encoding='utf-8') as file:
        json.dump(books, file, indent=2)

# -------------------------------
# View All Books
# -------------------------------

def view_all_books(books):
    if not books:
        print("❌ No books in the library.")
        return
    print("\n📚 All Books in Library:")
    print("=" * 50)
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {book['status']}")
    print("=" * 50)

# -------------------------------
# Add a Book
# -------------------------------

def add_book(books):
    next_id = max((int(book["id"]) for book in books), default=0) + 1
    title = input("📘 Enter book title: ").strip()
    author = input("✍️ Enter author name: ").strip()
    new_book = {
        "id": str(next_id),
        "title": title,
        "author": author,
        "status": "Available"
    }
    books.append(new_book)
    print(f"✅ Book '{title}' added successfully.")

# -------------------------------
# Search for a Book
# -------------------------------

def search_for_book(books):
    search_term = input("🔎 Enter book title or author to search: ").strip().lower()
    found_books = [book for book in books if search_term in book['title'].lower() or search_term in book['author'].lower()]
    if found_books:
        print(f"\n✅ Found {len(found_books)} matching book(s):")
        for book in found_books:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {book['status']}")
    else:
        print("❌ No matching books found.")

# -------------------------------
# Lend a Book
# -------------------------------

def lend_book(books):
    book_id = input("📤 Enter book ID to lend: ").strip()
    for book in books:
        if book["id"] == book_id:
            if book["status"].lower() == "available":
                book["status"] = "Lent"
                print(f"📕 Book '{book['title']}' has been lent out.")
            else:
                print(f"⚠️ Book '{book['title']}' is already lent.")
            return
    print("❌ Book ID not found.")

# -------------------------------
# Return a Book
# -------------------------------

def return_book(books):
    book_id = input("📥 Enter book ID to return: ").strip()
    for book in books:
        if book["id"] == book_id:
            if book["status"].lower() == "lent":
                book["status"] = "Available"
                print(f"📗 Book '{book['title']}' has been returned.")
            else:
                print(f"ℹ️ Book '{book['title']}' was not lent.")
            return
    print("❌ Book ID not found.")

# -------------------------------
# Remove a Book
# -------------------------------

def remove_book(books):
    book_id = input("🗑️ Enter book ID to remove: ").strip()
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print(f"❌ Book '{book['title']}' removed from library.")
            return
    print("❌ Book ID not found.")

# -------------------------------
# List Borrowed Books
# -------------------------------

def list_borrowed_books(books):
    borrowed = [book for book in books if book["status"].lower() == "lent"]
    print("\n📕 Borrowed Books:")
    if not borrowed:
        print("No books are currently lent.")
    else:
        for book in borrowed:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")

# -------------------------------
# List Available Books
# -------------------------------

def list_available_books(books):
    available = [book for book in books if book["status"].lower() == "available"]
    print("\n📗 Available Books:")
    if not available:
        print("No books available.")
    else:
        for book in available:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")

# -------------------------------
# Main Program Loop
# -------------------------------

def main():
    books = load_books()
    while True:
        print("\n📖 Library Management System")
        print("1. View All Books")
        print("2. Add a Book")
        print("3. Search for a Book")
        print("4. Lend a Book")
        print("5. Return a Book")
        print("6. Remove a Book")
        print("7. List Borrowed Books")
        print("8. List Available Books")
        print("9. Save and Exit")

        choice = input("👉 Enter your choice (1-9): ").strip()

        if choice == "1":
            view_all_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            search_for_book(books)
        elif choice == "4":
            lend_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            remove_book(books)
        elif choice == "7":
            list_borrowed_books(books)
        elif choice == "8":
            list_available_books(books)
        elif choice == "9":
            save_books(books)
            print("📦 Books saved. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
