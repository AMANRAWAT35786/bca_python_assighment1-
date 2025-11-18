
# Name: Aman Rawat
# Roll No: 2501060006
# Course: BCA (AI & DS)
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-2 Mini Project
# Title: Library Inventory & Borrowing System (CLI)
# Date: 17-11-2025


import csv
import os


# DATA STRUCTURES


# books dictionary: book_id → {title, author, copies}
books = {}

# borrowed dictionary: student_name → list of book_ids
borrowed = {}

# set of student names
student_names = set()



# HELPER FUNCTIONS


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """Display main menu."""
    print("\n" + "="*60)
    print("📚 LIBRARY BOOK MANAGER")
    print("="*60)
    print("1. Add / Update Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Borrowed Records")
    print("7. Save Books & Records to CSV")
    print("8. Load Books & Records from CSV")
    print("9. Load Sample Data (Demo)")
    print("0. Exit")
    print("="*60)



# TASK 2 – ADD / UPDATE BOOK


def add_book():
    """Add a new book or update copies."""
    print("\n--- Add / Update Book ---")

    book_id = input("Enter Book ID (e.g., B101): ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    try:
        copies = int(input("Enter number of copies: "))
        if copies < 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid number of copies.")
        return

    if book_id in books:
        books[book_id]["copies"] += copies
        print(f"✔ Updated: {book_id} now has {books[book_id]['copies']} copies.")
    else:
        books[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"✔ Book {book_id} added successfully.")



# TASK 3 – VIEW & SEARCH BOOKS


def view_books():
    """Display all books in formatted table."""
    print("\n--- Library Books ---")

    if not books:
        print("No books available.")
        return

    print(f"{'Book ID':<10}{'Title':<30}{'Author':<20}{'Copies':<6}")
    print("-" * 70)

    for bid, info in books.items():
        print(f"{bid:<10}{info['title'][:28]:<30}{info['author'][:18]:<20}{info['copies']:<6}")

    print("-" * 70)


def search_book():
    """Search book by ID or title keyword."""
    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title Keyword")

    choice = input("Choose option (1/2): ").strip()

    if choice == "1":
        bid = input("Enter Book ID: ").strip()
        info = books.get(bid)

        if info:
            print(f"✔ Found: {bid} → {info['title']} ({info['author']}) Copies: {info['copies']}")
        else:
            print("❌ Book ID not found.")

    elif choice == "2":
        keyword = input("Enter keyword: ").lower().strip()
        results = [(bid, info) for bid, info in books.items()
                   if keyword in info["title"].lower()]

        if results:
            print(f"\nFound {len(results)} result(s):")
            for bid, info in results:
                print(f"{bid}: {info['title']} by {info['author']} ({info['copies']} copies)")
        else:
            print("❌ No matching titles found.")
    else:
        print("❌ Invalid option.")



# TASK 4 – BORROW BOOK


def borrow_book():
    """Borrow a book and update records."""
    print("\n--- Borrow Book ---")

    student = input("Enter Student Name: ").strip()
    book_id = input("Enter Book ID: ").strip()

    if book_id not in books:
        print("❌ Book not found.")
        return

    if books[book_id]["copies"] <= 0:
        print("❌ No copies left for this book.")
        return

    # Update book and record
    books[book_id]["copies"] -= 1
    borrowed.setdefault(student, []).append(book_id)
    student_names.add(student)

    print(f"✔ {student} borrowed {book_id} ({books[book_id]['title']}).")



# TASK 5 – RETURN BOOK + LIST COMPREHENSION


def return_book():
    """Return a book and update inventory."""
    print("\n--- Return Book ---")

    student = input("Enter Student Name: ").strip()

    if student not in borrowed or len(borrowed[student]) == 0:
        print("❌ No borrowed books under this name.")
        return

    print(f"Borrowed books: {borrowed[student]}")
    book_id = input("Enter Book ID to return: ").strip()

    if book_id not in borrowed[student]:
        print("❌ This student didn't borrow that book.")
        return

    borrowed[student].remove(book_id)
    books[book_id]["copies"] += 1

    print(f"✔ {student} returned {book_id}. Updated copies: {books[book_id]['copies']}")


def view_borrowed():
    """Display all borrowed records using list comprehension."""
    print("\n--- Borrowed Records ---")

    if not borrowed or all(len(v) == 0 for v in borrowed.values()):
        print("No borrowed books.")
        return

    lines = [f"{student} → {', '.join(book_list)}"
             for student, book_list in borrowed.items() if book_list]

    for line in lines:
        print(line)



# CSV SAVE & LOAD


def save_to_csv():
    """Save books & borrowed data into CSV."""
    # Save books
    try:
        with open("books.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["book_id", "title", "author", "copies"])
            for bid, info in books.items():
                writer.writerow([bid, info["title"], info["author"], info["copies"]])
        print("✔ Books saved to books.csv")
    except:
        print("❌ Error saving books!")

    # Save borrowed
    try:
        with open("borrowed.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["student", "book_id"])
            for student, book_ids in borrowed.items():
                for bid in book_ids:
                    writer.writerow([student, bid])
        print("✔ Borrowed records saved to borrowed.csv")
    except:
        print("❌ Error saving borrowed records!")


def load_from_csv():
    """Load books & borrowed data from CSV."""
    # Load books
    if not os.path.exists("books.csv"):
        print("❌ books.csv not found.")
    else:
        with open("books.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            books.clear()
            for row in reader:
                books[row["book_id"]] = {
                    "title": row["title"],
                    "author": row["author"],
                    "copies": int(row["copies"])
                }
        print("✔ Books loaded.")

    # Load borrowed
    if not os.path.exists("borrowed.csv"):
        print("❌ borrowed.csv not found.")
    else:
        with open("borrowed.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            borrowed.clear()
            for row in reader:
                student = row["student"]
                bid = row["book_id"]
                borrowed.setdefault(student, []).append(bid)
        print("✔ Borrowed records loaded.")



# SAMPLE DATA (DEMO)


def load_sample_data():
    """Load 5 books for demo/testing."""
    books.clear()
    books.update({
        "B101": {"title": "Python Programming", "author": "John Doe", "copies": 3},
        "B102": {"title": "Data Structures", "author": "Jane Smith", "copies": 2},
        "B103": {"title": "Algorithms", "author": "Cormen", "copies": 1},
        "B104": {"title": "Database Systems", "author": "Elmasri", "copies": 4},
        "B105": {"title": "Operating Systems", "author": "Tanenbaum", "copies": 2},
    })
    borrowed.clear()
    student_names.clear()
    print("✔ Sample data loaded.")



# MAIN LOOP


def main():
    clear_screen()
    print("Welcome to Library Manager CLI")

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            view_borrowed()
        elif choice == "7":
            save_to_csv()
        elif choice == "8":
            load_from_csv()
        elif choice == "9":
            load_sample_data()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option!")

        input("\nPress Enter to continue...")
        clear_screen()


if __name__ == "__main__":
    main()
