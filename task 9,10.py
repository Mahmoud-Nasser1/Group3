import json

DB_FILE = "library.json"

def load_books():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(DB_FILE, "w") as file:
        json.dump(books, file, indent=2)

def list_available_books(books):
    print("\nAvailable Books:")
    available_books = [book for book in books if book['status'] == "Available"]
    if not available_books:
        print("No books available.")
    else:
        for book in available_books:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")

def main():
    books = load_books()
    while True:
        print("\nLibrary Management System")
        print("1. View All Books")
        print("2. Add a Book")
        print("3. Search for a Book")
        print("4. Lend a Book")
        print("5. Return a Book")
        print("6. Remove a Book")
        print("7. List Borrowed Books")
        print("8. List Available Books")
        print("9. Save and Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == "8":
            list_available_books(books)
        elif choice == "9":
            save_books(books)
            print("Books saved. Goodbye!")
            break
        else:
            print("Option not implemented yet.")

if __name__ == "__main__":
    main()
