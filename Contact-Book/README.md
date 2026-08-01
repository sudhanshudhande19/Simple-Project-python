# 📇 Contact Book

A simple command-line **Contact Book** application built in Python. It lets you add, view, search, update, and delete contacts — all stored in memory during a single session.

## ✨ Features

- **Add Contact** — Save a new contact with name, phone number, and email
- **View Contacts** — List all saved contacts
- **Search Contact** — Find a contact by name
- **Update Contact** — Edit an existing contact's phone number and email
- **Delete Contact** — Remove a contact by name
- **Input Validation** — Phone numbers must be exactly 10 digits; invalid menu choices are handled gracefully

## 🛠️ Tech Stack

- **Language:** Python 3
- **Data Structure:** List of dictionaries (in-memory storage)

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

```bash
git clone https://github.com/sudhanshudhande19/Contact-Book.git
cd Contact-Book
```

### Run the App

```bash
python contact_book.py
```

## 📖 Usage

Once you run the script, you'll see a menu:

```
=== Contact Book ===
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
====================
```

Enter the number corresponding to the action you want to perform, and follow the prompts.

## 📂 Project Structure

```
Contact-Book/
├── contact_book.py   # Main application logic
└── README.md          # Project documentation
```

## 🔮 Future Improvements

- Persist contacts to a file (JSON/CSV) or database so data isn't lost on exit
- Add duplicate-contact detection
- Add email format validation
- Build a GUI or web-based version

## 👤 Author

**Sudhanshu Dhande**
[@sudhanshudhande19](https://github.com/sudhanshudhande19)
