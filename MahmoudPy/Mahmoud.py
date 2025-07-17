import json
import os

DB_FILE = "library.json"

# -------------------------------
# Task 1: Load and Save Functions
# -------------------------------

def load_books():
    """Load books from the JSON database."""
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    """Save books to the JSON database."""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4)

# ----------------------
# Task 2: Add Book
# ----------------------

def add_book():
    books = load_books()

    # Automatically assign next available ID
    if books:
        next_id = max(book['id'] for book in books) + 1
    else:
        next_id = 1

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    new_book = {
        "id": next_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(new_book)
    save_books(books)
    print(f"Book '{title}' added successfully.")

# ----------------------------
# Task 3: View All Books
# ----------------------------

def view_all_books():
    books = load_books()
    if not books:
        print("No books in the library.")
        return

    print("\nAll Books in Library:")
    print("="*50)
    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {book['status']}")
        print("-" * 50)

# --------------------
# Main App Loop
# --------------------

def main():
    while True:
        print("\nLibrary Menu")
        print("1. View All Books")
        print("2. Add New Book")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_all_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
