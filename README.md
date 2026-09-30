# Smart Library Management System

## About the Project

The **Smart Library Management System** is a simple, menu-driven Python project designed to manage common library activities in an organized way.

The project allows users to manage books and students, search for books, issue and return books, calculate fines, and view useful library statistics.

The main aim of the project is to apply basic Python programming concepts to a practical, real-life problem.

## Features

### Book Management

* Add new books
* View all books
* Search books by:

  * Book ID
  * Title
  * Author
  * Category
* Update book details
* Remove books
* View only available books
* View books according to category

### Student Management

* Add students
* View registered students
* Search students by ID
* View the number of books borrowed by each student

### Library Operations

* Issue books to students
* Return books
* Renew borrowed books
* View books borrowed by a particular student
* Prevent a student from borrowing more than 3 books
* Prevent an already-issued book from being issued again

### Additional Features

* Fine calculator for late returns
* Library dashboard
* Total, available and issued book count
* Category-wise book count
* Most borrowed book tracker

## Python Concepts Used

This project was created using basic Python concepts:

* Variables
* Input and output
* Lists
* Dictionaries
* `for` and `while` loops
* `if-elif-else` statements
* Functions
* String operations
* Basic calculations

No external libraries or advanced programming concepts are required.

## How the System Works

The program starts with a main menu containing different library operations.

The user selects an option by entering its number. The corresponding function is then executed.

Books are stored using dictionaries inside a list. Each book contains information such as its ID, title, author, category, availability status and issue count.

Students are also stored using dictionaries inside a list. Each student has an ID, name, branch and a list of borrowed book IDs.

The system uses conditions to check situations such as whether a book is available, whether a student exists, or whether a student has already reached the borrowing limit.

## Sample Menu

```text
===================================================
                  MAIN MENU
===================================================

1. Add Book
2. View All Books
3. Search Library
4. Update Book
5. Remove Book
6. Add Student
7. View Students
8. Search Student
9. Issue Book
10. Return Book
11. Renew Book
12. View Borrowed Books
13. Fine Calculator
14. Library Dashboard
15. Most Borrowed Book
16. View Available Books
17. Books by Category
18. Exit
```

## How to Run

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open `smart_library_management.py`.
4. Run the Python file.
5. Select options from the main menu and follow the instructions.

## Future Scope

The project can be further improved by adding:

* Login system for librarians and students
* Database connectivity
* Automatic due dates
* Individual fine records
* Graphical user interface
* Book reservation system
* Permanent data storage

## Project Objective

The objective of this project is to understand how basic Python programming concepts can be combined to create a functional application based on a real-world problem.

---

**Project:** Smart Library Management System
**Language:** Python
**Level:** First-Year CSE Project

