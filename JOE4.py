import json

def load_books():
    try:
        with open('library.json', 'r') as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []

def search_for_book():
    books = load_books()
    if not books:
        print("❌ No books found in the library.")
        return

    search_term = input("🔎 Enter book title or author to search: ").strip().lower()
    found_books = []

    for book in books:
        title = book.get("title", "").lower()
        author = book.get("author", "").lower()
        if search_term in title or search_term in author:
            found_books.append(book)

    if found_books:
        print(f"\n✅ Found {len(found_books)} matching book(s):")
        for book in found_books:
            print(f"ID: {book.get('id')} | Title: {book.get('title')} | Author: {book.get('author')} | Status: {book.get('status')}")
    else:
        print("❌ No matching books found.")