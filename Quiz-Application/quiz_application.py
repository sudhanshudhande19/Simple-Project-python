
# ==========================================
#          QUIZ APPLICATION
# ==========================================

print("=======================")
print("        Welcome        ")
print("    Quiz Application   ")
print("=======================")


# List to store marks for correct answers
my_list = []

# Total number of questions
Total_Question = 10


# Function to store all quiz questions
def application(que):

    que = {
        "Q1": "Q1. Who developed Python programming language?",
        "Q2": "Q2. In which year was Python first released?",
        "Q3": "Q3. Python is considered as...",
        "Q4": "Q4. Which of the following is true about Python?",
        "Q5": "Q5. Python is...",
        "Q6": "Q6. Which of the following is NOT a feature of Python?",
        "Q7": "Q7. What type of programming does Python support?",
        "Q8": "Q8. Python files are saved with which extension?",
        "Q9": "Q9. Which of the following is used to define a block of code in Python?",
        "Q10": "Q10. Python is maintained by..."
    }

    return que


# Calling the function
kk = application({})


# Ask the user whether they want to start the quiz
option = input("Start the Quiz Application (Yes/No) = ")


# Start the quiz if user enters Yes
if option.lower() == "yes":

    # Take user's basic information
    name = input("Enter the Name = ")
    rollno = int(input("Enter the Roll No = "))

    print()
    print("===== Start Application =====")
    print()


    # ==========================================
    # Question 1
    # ==========================================

    print(kk["Q1"])
    print()

    a1 = "A) Dennis Ritchie"
    b1 = "B) James Gosling"
    c1 = "C) Guido van Rossum"
    d1 = "D) Bjarne Stroustrup"

    print(a1)
    print(b1)
    print(c1)
    print(d1)

    Enter_option1 = input("Enter Option = ")

    if Enter_option1.lower() == "c":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 2
    # ==========================================

    print(kk["Q2"])
    print()

    a2 = "A) 1989"
    b2 = "B) 1991"
    c2 = "C) 1995"
    d2 = "D) 2000"

    print(a2)
    print(b2)
    print(c2)
    print(d2)

    Enter_option2 = input("Enter Option = ")

    if Enter_option2.lower() == "b":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 3
    # ==========================================

    print(kk["Q3"])
    print()

    a3 = "A) Low-level language"
    b3 = "B) High-level language"
    c3 = "C) Assembly language"
    d3 = "D) Machine language"

    print(a3)
    print(b3)
    print(c3)
    print(d3)

    Enter_option3 = input("Enter Option = ")

    if Enter_option3.lower() == "b":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 4
    # ==========================================

    print(kk["Q4"])
    print()

    a4 = "A) Python is compiled only"
    b4 = "B) Python is interpreted only"
    c4 = "C) Python is both compiled and interpreted"
    d4 = "D) Python is neither compiled nor interpreted"

    print(a4)
    print(b4)
    print(c4)
    print(d4)

    Enter_option4 = input("Enter Option = ")

    if Enter_option4.lower() == "c":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 5
    # ==========================================

    print(kk["Q5"])
    print()

    a5 = "A) Case-sensitive language"
    b5 = "B) Case-insensitive language"
    c5 = "C) Depends on compiler"
    d5 = "D) None of the above"

    print(a5)
    print(b5)
    print(c5)
    print(d5)

    Enter_option5 = input("Enter Option = ")

    if Enter_option5.lower() == "a":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 6
    # ==========================================

    print(kk["Q6"])
    print()

    a6 = "A) Easy to learn"
    b6 = "B) Platform independent"
    c6 = "C) Supports OOP"
    d6 = "D) Requires manual memory management"

    print(a6)
    print(b6)
    print(c6)
    print(d6)

    Enter_option6 = input("Enter Option = ")

    if Enter_option6.lower() == "d":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 7
    # ==========================================

    print(kk["Q7"])
    print()

    a7 = "A) Procedural"
    b7 = "B) Object-Oriented"
    c7 = "C) Functional"
    d7 = "D) All of the above"

    print(a7)
    print(b7)
    print(c7)
    print(d7)

    Enter_option7 = input("Enter Option = ")

    if Enter_option7.lower() == "d":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 8
    # ==========================================

    print(kk["Q8"])
    print()

    a8 = "A) .py"
    b8 = "B) .python"
    c8 = "C) .pyt"
    d8 = "D) .pt"

    print(a8)
    print(b8)
    print(c8)
    print(d8)

    Enter_option8 = input("Enter Option = ")

    if Enter_option8.lower() == "a":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 9
    # ==========================================

    print(kk["Q9"])
    print()

    a9 = "A) Curly braces {}"
    b9 = "B) Parentheses ()"
    c9 = "C) Indentation"
    d9 = "D) Semicolon ;"

    print(a9)
    print(b9)
    print(c9)
    print(d9)

    Enter_option9 = input("Enter Option = ")

    if Enter_option9.lower() == "c":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    # Question 10
    # ==========================================

    print(kk["Q10"])
    print()

    a10 = "A) Oracle"
    b10 = "B) Microsoft"
    c10 = "C) Python Software Foundation"
    d10 = "D) Google"

    print(a10)
    print(b10)
    print(c10)
    print(d10)

    Enter_option10 = input("Enter Option = ")

    if Enter_option10.lower() == "c":
        print("Correct")
        my_list.append(1)
    else:
        print("Wrong")


    print("-----------------------------")
    print()


    # ==========================================
    #             FINAL RESULT
    # ==========================================

    print("============ Result ============")

    # Display user's information
    print("Name =", name)
    print("Roll No =", rollno)

    # Display total questions
    print("Total Questions =", Total_Question)

    # Calculate correct answers
    correct = len(my_list)
    print("Correct =", correct)

    # Calculate wrong answers
    Wrong = Total_Question - correct
    print("Wrong =", Wrong)

    # Display score
    print("Score =", correct, "/", Total_Question)

    # Calculate percentage
    per = (correct / Total_Question) * 100
    print("Percentage =", per, "%")

    print("===============================")
    print("========= Thank You ===========")

    # Exit the program
    exit()


# If the user does not want to start the quiz
else:
    print("Thank You")
    exit()
