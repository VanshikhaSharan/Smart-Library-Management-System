print("===================================================")
print("           SMART LIBRARY MANAGEMENT SYSTEM")
print("===================================================")

# ---------------- DATA ----------------

books = [
    {
        "id": 101,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Fiction",
        "status": "Available",
        "issue_count": 0
    },
    {
        "id": 102,
        "title": "Wings of Fire",
        "author": "A.P.J. Abdul Kalam",
        "category": "Biography",
        "status": "Available",
        "issue_count": 0
    },
    {
        "id": 103,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "category": "Computer",
        "status": "Available",
        "issue_count": 0
    },
    {
        "id": 104,
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "category": "Fiction",
        "status": "Available",
        "issue_count": 0
    }
]

students = [
    {
        "id": 1,
        "name": "Inika",
        "branch": "CSE",
        "borrowed_books": []
    }
]


# ---------------- BOOK MANAGEMENT ----------------

def add_book():
    print("\n---------- ADD NEW BOOK ----------")

    book_id = int(input("Enter book ID: "))

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter category: ")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "status": "Available",
        "issue_count": 0
    }

    books.append(new_book)

    print("\nBook added successfully!")


def view_books():
    print("\n---------- ALL BOOKS ----------")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print("\nBook ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Category:", book["category"])
        print("Status:", book["status"])
        print("Times Issued:", book["issue_count"])


def remove_book():
    print("\n---------- REMOVE BOOK ----------")

    book_id = int(input("Enter book ID: "))

    for book in books:

        if book["id"] == book_id:

            if book["status"] == "Issued":
                print("This book is currently issued and cannot be removed.")
                return

            books.remove(book)
            print("Book removed successfully.")
            return

    print("Book not found.")


def update_book():
    print("\n---------- UPDATE BOOK ----------")

    book_id = int(input("Enter book ID: "))

    for book in books:

        if book["id"] == book_id:

            print("\nCurrent Details:")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Category:", book["category"])

            print("\nEnter new details:")

            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            book["category"] = input("New category: ")

            print("Book details updated successfully.")
            return

    print("Book not found.")


# ---------------- SEARCH ----------------

def search_book():

    print("\n---------- SEARCH LIBRARY ----------")

    print("1. Search by Book ID")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Category")

    choice = input("\nEnter your choice: ")

    found = False

    if choice == "1":

        book_id = int(input("Enter book ID: "))

        for book in books:

            if book["id"] == book_id:

                print("\nBook Found!")
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Category:", book["category"])
                print("Status:", book["status"])

                found = True

    elif choice == "2":

        title = input("Enter title: ").lower()

        for book in books:

            if title in book["title"].lower():

                print("\nBook Found!")
                print("Book ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Category:", book["category"])
                print("Status:", book["status"])

                found = True

    elif choice == "3":

        author = input("Enter author name: ").lower()

        for book in books:

            if author in book["author"].lower():

                print("\nBook Found!")
                print("Book ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Category:", book["category"])
                print("Status:", book["status"])

                found = True

    elif choice == "4":

        category = input("Enter category: ").lower()

        for book in books:

            if category in book["category"].lower():

                print("\nBook Found!")
                print("Book ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", book["status"])

                found = True

    else:
        print("Invalid choice.")
        return

    if found == False:
        print("\nNo matching book found.")


# ---------------- STUDENT MANAGEMENT ----------------

def add_student():

    print("\n---------- ADD STUDENT ----------")

    student_id = int(input("Enter student ID: "))

    for student in students:

        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter student name: ")
    branch = input("Enter branch: ")

    new_student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "borrowed_books": []
    }

    students.append(new_student)

    print("Student registered successfully!")


def view_students():

    print("\n---------- REGISTERED STUDENTS ----------")

    if len(students) == 0:
        print("No students registered.")
        return

    for student in students:

        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Books Borrowed:", len(student["borrowed_books"]))


def search_student():

    print("\n---------- SEARCH STUDENT ----------")

    student_id = int(input("Enter student ID: "))

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Books Borrowed:", len(student["borrowed_books"]))

            return

    print("Student not found.")


# ---------------- ISSUE BOOK ----------------

def issue_book():

    print("\n---------- ISSUE BOOK ----------")

    student_id = int(input("Enter student ID: "))
    book_id = int(input("Enter book ID: "))

    selected_student = None
    selected_book = None

    for student in students:

        if student["id"] == student_id:
            selected_student = student

    for book in books:

        if book["id"] == book_id:
            selected_book = book

    if selected_student == None:
        print("Student not found.")
        return

    if selected_book == None:
        print("Book not found.")
        return

    if selected_book["status"] == "Issued":
        print("Sorry, this book is already issued.")
        return

    if len(selected_student["borrowed_books"]) >= 3:
        print("A student can borrow a maximum of 3 books.")
        return

    selected_book["status"] = "Issued"

    selected_student["borrowed_books"].append(book_id)

    selected_book["issue_count"] = selected_book["issue_count"] + 1

    print("\nBook issued successfully!")
    print("Student:", selected_student["name"])
    print("Book:", selected_book["title"])


# ---------------- RETURN BOOK ----------------

def return_book():

    print("\n---------- RETURN BOOK ----------")

    student_id = int(input("Enter student ID: "))
    book_id = int(input("Enter book ID: "))

    selected_student = None
    selected_book = None

    for student in students:

        if student["id"] == student_id:
            selected_student = student

    for book in books:

        if book["id"] == book_id:
            selected_book = book

    if selected_student == None:
        print("Student not found.")
        return

    if selected_book == None:
        print("Book not found.")
        return

    if book_id not in selected_student["borrowed_books"]:
        print("This book was not issued to this student.")
        return

    selected_student["borrowed_books"].remove(book_id)

    selected_book["status"] = "Available"

    print("\nBook returned successfully!")


# ---------------- RENEW BOOK ----------------

def renew_book():

    print("\n---------- RENEW BOOK ----------")

    student_id = int(input("Enter student ID: "))
    book_id = int(input("Enter book ID: "))

    for student in students:

        if student["id"] == student_id:

            if book_id in student["borrowed_books"]:

                print("\nBook renewed successfully!")
                print("Borrowing period has been extended.")

                return

            else:
                print("This student has not borrowed this book.")
                return

    print("Student not found.")


# ---------------- BORROWED BOOKS ----------------

def borrowed_books():

    print("\n---------- MY BORROWED BOOKS ----------")

    student_id = int(input("Enter student ID: "))

    for student in students:

        if student["id"] == student_id:

            print("\nStudent:", student["name"])

            if len(student["borrowed_books"]) == 0:
                print("No books borrowed.")
                return

            for book_id in student["borrowed_books"]:

                for book in books:

                    if book["id"] == book_id:

                        print("\nBook ID:", book["id"])
                        print("Title:", book["title"])
                        print("Author:", book["author"])

            return

    print("Student not found.")


# ---------------- FINE CALCULATOR ----------------

def fine_check():

    print("\n---------- FINE CALCULATOR ----------")

    days_late = int(input("Enter number of days late: "))

    if days_late <= 3:

        fine = 0

    else:

        fine = (days_late - 3) * 5

    print("\nDays Late:", days_late)
    print("Fine: Rs.", fine)


# ---------------- STATISTICS ----------------

def library_statistics():

    print("\n---------- LIBRARY DASHBOARD ----------")

    total_books = len(books)
    available_books = 0
    issued_books = 0

    for book in books:

        if book["status"] == "Available":
            available_books = available_books + 1

        elif book["status"] == "Issued":
            issued_books = issued_books + 1

    print("\nTotal Books:", total_books)
    print("Available Books:", available_books)
    print("Issued Books:", issued_books)
    print("Registered Students:", len(students))

    print("\n---------- CATEGORY COUNT ----------")

    categories = []

    for book in books:

        if book["category"] not in categories:
            categories.append(book["category"])

    for category in categories:

        count = 0

        for book in books:

            if book["category"] == category:
                count = count + 1

        print(category, ":", count)


# ---------------- MOST BORROWED BOOK ----------------

def most_borrowed_book():

    print("\n---------- MOST BORROWED BOOK ----------")

    if len(books) == 0:
        print("No books available.")
        return

    highest = books[0]

    for book in books:

        if book["issue_count"] > highest["issue_count"]:
            highest = book

    print("\nMost Borrowed Book:", highest["title"])
    print("Author:", highest["author"])
    print("Times Issued:", highest["issue_count"])


# ---------------- AVAILABLE BOOKS ----------------

def available_books():

    print("\n---------- AVAILABLE BOOKS ----------")

    found = False

    for book in books:

        if book["status"] == "Available":

            print("\nID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Category:", book["category"])

            found = True

    if found == False:
        print("No books are currently available.")


# ---------------- CATEGORY BOOKS ----------------

def category_books():

    print("\n---------- BOOKS BY CATEGORY ----------")

    category = input("Enter category: ").lower()

    found = False

    for book in books:

        if book["category"].lower() == category:

            print("\nID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])

            found = True

    if found == False:
        print("No books found in this category.")


# ---------------- MAIN MENU ----------------

while True:

    print("\n")
    print("===================================================")
    print("                  MAIN MENU")
    print("===================================================")

    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Library")
    print("4. Update Book")
    print("5. Remove Book")
    print("6. Add Student")
    print("7. View Students")
    print("8. Search Student")
    print("9. Issue Book")
    print("10. Return Book")
    print("11. Renew Book")
    print("12. View Borrowed Books")
    print("13. Fine Calculator")
    print("14. Library Dashboard")
    print("15. Most Borrowed Book")
    print("16. View Available Books")
    print("17. Books by Category")
    print("18. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        remove_book()

    elif choice == "6":
        add_student()

    elif choice == "7":
        view_students()

    elif choice == "8":
        search_student()

    elif choice == "9":
        issue_book()

    elif choice == "10":
        return_book()

    elif choice == "11":
        renew_book()

    elif choice == "12":
        borrowed_books()

    elif choice == "13":
        fine_check()

    elif choice == "14":
        library_statistics()

    elif choice == "15":
        most_borrowed_book()

    elif choice == "16":
        available_books()

    elif choice == "17":
        category_books()

    elif choice == "18":
        print("\nThank you for using Smart Library Management System!")
        print("Have a great day!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 18.")