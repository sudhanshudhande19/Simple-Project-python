# 📚 Library Management System

A simple console-based **Library Management System** built in Python using dictionaries and lists — no external database required. This project allows users to add, view, search, issue, return, and delete books, while also tracking student book-issue records.

---

## ✨ Features

- **Add Book** — Add a new book with ID, name, author, category, and quantity.
- **View Book** — Display all books currently in the library along with their availability.
- **Search Book** — Search for a book by name and view its details.
- **Issue Book** — Issue a book to a student (with mobile number validation).
- **Return Book** — Return an issued book and update available quantity.
- **Delete Book** — Remove a book record from the library using its Book ID.
- **Exit** — Safely exit the program.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Data Storage:** In-memory (Python lists & dictionaries)
- **Interface:** Command Line Interface (CLI)

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3** installed on your system.

```bash
python --version
```

### Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/library-management-system.git
   cd library-management-system
   ```

2. Run the script:
   ```bash
   python library_management.py
   ```

---

## 📋 Menu Options

```
=====Library Management System=====
1. Add Book
2. View Book
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
====================================
```

---

## 📌 Sample Usage

```
Select The Option 1 to 7 = 1
Enter Add Book ID = 101
Enter The Add Book Name = Python Programming
Enter Author Name = John Doe
Enter Book Category = Programming
Enter The Quantity Book = 5
Book Add Successfully!
```

---

## 🧩 Project Structure

```
library-management-system/
│
├── library_management.py   # Main source code
└── README.md                # Project documentation
```


## 🔮 Future Improvements

- Add persistent storage using **JSON**, **CSV**, or **SQLite**.
- Add input validation and error handling (try/except) for numeric inputs.
- Improve search to check all records before declaring "not found."
- Build a **GUI** version using Tkinter or a web version using Flask/Django.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) if you want to contribute.

---

## 👤 Author

**Sudhanshu**
B.Tech CSE (AI & ML), Dr. Babasaheb Ambedkar Technological University (BATU), Lonere
