<div align="center">

<img src="assets/banner.svg" alt="Voting System in Python Banner" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-CLI%20Project-f09819?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-43e97b?style=for-the-badge)
![Made By](https://img.shields.io/badge/Made%20by-Sudhanshu%20Dhande-ff512f?style=for-the-badge)

<h3>🗳️ A simple Voting System project built using Python 🗳️</h3>

<p>
  <a href="#-features">Features</a> •
  <a href="#-how-the-project-works">How It Works</a> •
  <a href="#️-how-to-run">How to Run</a> •
  <a href="#-concepts-learned">Concepts</a> •
  <a href="#-author">Author</a>
</p>

</div>

---

## 📖 About

A simple **Voting System project built using Python**. This project allows users to vote for candidates after checking their age and voter ID. It also prevents duplicate voting and displays the final election result, including tie detection.

---

## 📌 Features

| | Feature |
|---|---|
| 👤 | Takes voter name, age, and voter ID |
| 🔞 | Checks whether the voter is eligible to vote |
| 🆔 | Prevents duplicate voting using voter ID |
| 🗳️ | Provides multiple candidate options |
| 📊 | Counts votes for each candidate |
| 🚫 | Includes NOTA option |
| 🏆 | Displays the election winner |
| 🤝 | Detects election ties |
| 🔄 | Allows multiple voters to vote |
| 💬 | Displays confirmation messages after voting |

---

## 🛠️ Technologies Used

<p>
  <img src="https://img.shields.io/badge/Python%203-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Dictionaries-f09819?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lists-43e97b?style=flat-square"/>
  <img src="https://img.shields.io/badge/Functions-4facfe?style=flat-square"/>
</p>

- **Python 3**
- Python Dictionaries
- Python Lists
- Functions
- `while` loop
- `if-elif-else` conditions
- User Input
- List Comprehension

---

## 👥 Candidates

The voting system currently contains four options:

1. Rahul
2. Amit
3. Priya
4. NOTA

---

## ⚙️ How the Project Works

### 1️⃣ Voter Information

The program asks the voter to enter:
- Voter Name
- Voter Age
- Voter ID Number

### 2️⃣ Eligibility Check

The voter must be **18 years or older** to vote.

```python
if age >= 18:
    # Voter is eligible
else:
    # Voter is not eligible
```

### 3️⃣ Duplicate Vote Prevention

The program stores voter IDs in a list.

```python
my_list = []
```

Before allowing a vote, it checks whether the voter ID already exists.

```python
if vote_id in my_list:
    print("You have already voted!")
```

This prevents the same voter from voting more than once.

### 4️⃣ Candidate Selection

The voter can select one of the available candidates.

```text
1. Rahul
2. Amit
3. Priya
4. NOTA
```

The selected candidate's vote count is increased by 1.

### 5️⃣ Voting Result

After voting is completed, the program displays the total votes received by each candidate.

```text
Rahul : 5 votes
Amit  : 3 votes
Priya : 7 votes
NOTA  : 1 votes
```

The program then finds the candidate with the highest number of votes.

### 6️⃣ Tie Detection

If two or more candidates have the same maximum votes, the program displays an election tie.

```text
ELECTION TIE
Candidates: ['Rahul', 'Priya']
Votes: 5
```

Otherwise, it displays the winner.

```text
WINNER: Priya
Votes: 7
```

---

## ▶️ How to Run

**Step 1: Install Python**

Make sure Python 3 is installed on your computer.

```bash
python --version
```

**Step 2: Clone the Repository**

```bash
git clone <your-github-repository-url>
```

**Step 3: Open the Project Folder**

```bash
cd Voting-System-Python
```

**Step 4: Run the Program**

```bash
python voting_system.py
```

---

## 📂 Project Structure

```text
Voting-System-Python/
│
├── assets/
│   └── banner.svg
├── README.md
└── voting_system.py
```

---

## 💡 Concepts Learned

This project helped practice the following Python concepts:

- Variables
- Data Types
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- User Input
- List Membership
- List Comprehension
- Dictionary Methods
- `max()` function
- String methods such as `.lower()`
- Basic project structure

---

## 🚀 Future Improvements

The project can be improved further by adding:

- 🔐 Password or OTP-based voter verification
- 💾 Database storage using SQLite/MySQL
- 🖥️ GUI using Tkinter or PyQt
- 📈 Graphical representation of voting results
- 📝 Saving voter records to a file
- 🔑 Better voter ID validation
- 🛡️ Improved data security
- 🌐 Web-based voting system

---

## 👨‍💻 Author

<div align="center">

**Sudhanshu Dhande**
B.Tech – Artificial Intelligence

</div>

---

## 📄 License

This project is created for **learning and educational purposes**.

<div align="center">

⭐ *If you like this project, don't forget to give it a star!* ⭐

</div>