<div align="center">

<img src="assets/banner.svg" alt="Library Management System Banner" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-CLI%20Project-ff9a00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-43e97b?style=for-the-badge)
![Made By](https://img.shields.io/badge/Made%20by-Sudhanshu-ffd76a?style=for-the-badge)

<h3>📚 A simple console-based Library Management System built in Python 📚</h3>

<p>
  <a href="#-features">Features</a> •
  <a href="#️-tech-stack">Tech Stack</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-menu-options">Menu</a> •
  <a href="#-sample-usage">Sample Usage</a> •
  <a href="#-author">Author</a>
</p>

</div>

---

## 📖 About

A simple console-based **Library Management System** built in Python using dictionaries and lists — **no external database required**. This project allows users to add, view, search, issue, return, and delete books, while also tracking student book-issue records.

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| ➕ | **Add Book** | Add a new book with ID, name, author, category, and quantity |
| 👀 | **View Book** | Display all books currently in the library along with their availability |
| 🔍 | **Search Book** | Search for a book by name and view its details |
| 📤 | **Issue Book** | Issue a book to a student (with mobile number validation) |
| 📥 | **Return Book** | Return an issued book and update available quantity |
| 🗑️ | **Delete Book** | Remove a book record from the library using its Book ID |
| 🚪 | **Exit** | Safely exit the program |

---

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python%203-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Lists-ff9a00?style=flat-square"/>
  <img src="https://img.shields.io/badge/Dictionaries-43e97b?style=flat-square"/>
  <img src="https://img.shields.io/badge/CLI-4facfe?style=flat-square"/>
</p>

| Component | Details |
|---|---|
| **Language** | Python 3 |
| **Data Storage** | In-memory (Python lists & dictionaries) |
| **Interface** | Command Line Interface (CLI) |

---

## 🚀 Getting Started

### ✅ Prerequisites
Make sure you have **Python 3** installed on your system.

```bash
python --version
```

### ▶️ Run the Project

**1. Clone the repository:**
```bash
git clone https://github.com/<your-username>/library-management-system.git
cd library-management-system
```

**2. Run the script:**
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
├── assets/
│   └── banner.svg
├── library_management.py    # Main source code
└── README.md                # Project documentation
```

---

## 🔮 Future Improvements

- 🔹 Add persistent storage using **JSON**, **CSV**, or **SQLite**
- 🔹 Add input validation and error handling (`try/except`) for numeric inputs
- 🔹 Improve search to check all records before declaring "not found"
- 🔹 Build a **GUI** version using Tkinter or a web version using Flask/Django

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) if you want to contribute.

---

## 👤 Author

<div align="center">

**Sudhanshu**
B.Tech CSE (AI & ML), Dr. Babasaheb Ambedkar Technological University (BATU), Lonere

⭐ *If you like this project, don't forget to give it a star!* ⭐

</div>