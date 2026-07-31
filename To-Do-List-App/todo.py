# ---------------- TO-DO LIST APP ----------------

# Create an empty list to store tasks
task = []

# Run the program until the user chooses to exit
while True:

    # Display the menu
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    # Take the user's choice
    choice = input("Select The Option : ")

    # ---------------- Add Task ----------------
    if choice == "1":

        # Take task input from the user
        ad = input("Enter The Task : ")

        # Check if the task is empty
        if ad == "":
            print("Task Cannot Be Empty")

        else:
            # Add the task to the list
            task.append(ad)
            print("Task Added Successfully")

    # ---------------- View Tasks ----------------
    elif choice == "2":

        # Check if the task list is empty
        if len(task) == 0:
            print("No Tasks Available")

        else:
            # Display all tasks with numbering
            print("\n===== YOUR TASKS =====")

            for i in range(len(task)):
                print(f"{i + 1}. {task[i]}")

    # ---------------- Delete Task ----------------
    elif choice == "3":

        # Check if there are any tasks
        if len(task) == 0:
            print("No Tasks Available")

        else:
            # Display all tasks before deleting
            print("\n===== YOUR TASKS =====")

            for i in range(len(task)):
                print(f"{i + 1}. {task[i]}")

            try:
                # Take the task number to delete
                num = int(input("Enter Task Number To Delete : "))

                # Check if the task number is valid
                if 1 <= num <= len(task):

                    # Delete the selected task
                    deleted = task.pop(num - 1)

                    print(f"'{deleted}' Deleted Successfully")

                else:
                    print("Invalid Task Number")

            # Handle invalid input
            except ValueError:
                print("Please Enter a Valid Number")

    # ---------------- Exit Program ----------------
    elif choice == "4":

        print("Thank You For Using To-Do List App")
        print("Visit Again")
        break

    # ---------------- Invalid Choice ----------------
    else:
        print("Invalid Choice")