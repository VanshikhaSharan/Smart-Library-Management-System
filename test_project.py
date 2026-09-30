print("======================================")
print("       SMART LIBRARY TEST PROJECT")
print("======================================")

# Sample test data
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


# Test 1: Add Book
def test_add_book():
    new_book = {
        "id": 103,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "category": "Computer",
        "status": "Available",
        "issue_count": 0
    }

    books.append(new_book)

    if len(books) == 3:
        print("Test 1 - Add Book: PASS")
    else:
        print("Test 1 - Add Book: FAIL")


# Test 2: Search Book
def test_search_book():
    found = False

    for book in books:
        if book["title"].lower() == "the alchemist".lower():
            found = True

    if found:
        print("Test 2 - Search Book: PASS")
    else:
        print("Test 2 - Search Book: FAIL")


# Test 3: Issue Book
def test_issue_book():
    book = books[0]
    student = students[0]

    if book["status"] == "Available":
        book["status"] = "Issued"
        book["issue_count"] += 1
        student["borrowed_books"].append(book["id"])

    if book["status"] == "Issued" and book["id"] in student["borrowed_books"]:
        print("Test 3 - Issue Book: PASS")
    else:
        print("Test 3 - Issue Book: FAIL")


# Test 4: Return Book
def test_return_book():
    book = books[0]
    student = students[0]

    if book["id"] in student["borrowed_books"]:
        student["borrowed_books"].remove(book["id"])
        book["status"] = "Available"

    if book["status"] == "Available" and len(student["borrowed_books"]) == 0:
        print("Test 4 - Return Book: PASS")
    else:
        print("Test 4 - Return Book: FAIL")


# Test 5: Fine Calculator
def test_fine():
    late_days = 7

    if late_days <= 3:
        fine = 0
    else:
        fine = (late_days - 3) * 5

    if fine == 20:
        print("Test 5 - Fine Calculator: PASS")
    else:
        print("Test 5 - Fine Calculator: FAIL")


# Run all tests
print()

test_add_book()
test_search_book()
test_issue_book()
test_return_book()
test_fine()

print()
print("======================================")
print("          TESTING COMPLETED")
print("======================================")
