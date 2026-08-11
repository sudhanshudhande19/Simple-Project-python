
print("===========================")
print("         NOTES APP         ")
print("===========================")
print()

print("1. Add Note")
print("2. View Note")
print("3. Search Note")
print("4. Delete Note")
print("5. Exit")


# =========================
# ADD NOTE
# =========================

def add_note():

    note = input("Enter Your Note: ")

    with open("data.txt", "a") as file:
        file.write(note + "\n")

    print("Note Added Successfully!")


# =========================
# VIEW NOTE
# =========================

def view_note():

    with open("data.txt", "r") as file:
        notes = file.readlines()

    print()
    print("========== YOUR NOTES ==========")

    if len(notes) == 0:
        print("No Notes Found!")

    else:
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note.strip()}")

    print("================================")


# =========================
# SEARCH NOTE
# =========================

def search_note():

    keyword = input("Enter The Keyword: ")

    found = False

    with open("data.txt", "r") as file:

        for line in file:

            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

    if found:
        print("Searching The Note Successfully!")

    else:
        print("Keyword Not Found!")


# =========================
# DELETE NOTE
# =========================

def delete_note():

    with open("data.txt", "r") as file:
        notes = file.readlines()

    if len(notes) == 0:
        print("No Notes Available!")

        return

    print()
    print("========== YOUR NOTES ==========")

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")

    print("================================")

    option = int(input("Enter Note Number To Delete: "))

    if 1 <= option <= len(notes):

        deleted_note = notes.pop(option - 1)

        with open("data.txt", "w") as file:
            file.writelines(notes)

        print(f"Deleted Note: {deleted_note.strip()}")
        print("Note Deleted Successfully!")

    else:
        print("Invalid Note Number!")


# =========================
# MAIN PROGRAM
# =========================

while True:

    print()
    choice = int(input("Enter Your Choice = "))

    if choice == 1:

        add_note()

    elif choice == 2:

        view_note()

    elif choice == 3:

        search_note()

    elif choice == 4:

        delete_note()

    elif choice == 5:

        print("=================================")
        print("Thank you for using Notes App!")
        print("=================================")

        break

    else:

        print("Invalid Choice! Please try again.")