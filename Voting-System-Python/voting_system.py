
print("=============================")
print("  WELCOME TO VOTING SYSTEM   ")
print("=============================")

# Store all voter IDs to prevent duplicate voting
my_list = []


# Function to store voter information
def vote_system(vote):
    vote = {
        'name': '',
        'age': '',
        'vote_id': ''
    }
    return vote


kk = vote_system({})


# Function to create the candidate vote dictionary
def candidates(people):
    people = {
        'Rahul': 0,
        'Amit': 0,
        'Priya': 0,
        'NOTA': 0
    }
    return people


ll = candidates({})


# ================= VOTING SYSTEM =================

while True:

    # Get voter information
    name = input("Enter the Voter Name = ")
    age = int(input("Enter the Voter Age = "))
    vote_id = input("Enter the Voter ID Number = ")

    # Store voter information
    kk['name'] = name
    kk['age'] = age
    kk['vote_id'] = vote_id

    print()

    # Check whether the voter is eligible
    if age >= 18:

        # Check whether the voter has already voted
        if vote_id in my_list:
            print("You have already voted!")
            print("You cannot vote again.")
            exit()

        else:
            print("Checking eligibility...")
            print("----------- CANDIDATES ------------")
            print("1. Rahul")
            print("2. Amit")
            print("3. Priya")
            print("4. NOTA")
            print("-----------------------------------")
            print()

            # Ask the voter to select a candidate
            option = input("Enter Your Choice = ")

            # Count the vote according to the selected candidate
            if option == "1":
                ll['Rahul'] += 1
                print("Your vote has been successfully cast for Rahul.")

            elif option == "2":
                ll['Amit'] += 1
                print("Your vote has been successfully cast for Amit.")

            elif option == "3":
                ll['Priya'] += 1
                print("Your vote has been successfully cast for Priya.")

            elif option == "4":
                ll['NOTA'] += 1
                print("Your vote has been successfully cast for NOTA.")

            else:
                print("Please select the correct option.")
                exit()

            # Store the voter ID after a successful vote
            my_list.append(vote_id)

            print("Thank you for voting!")

            # Ask whether another voter wants to vote
            continue_voting = input(
                "Do you want to continue voting? (yes/no): "
            )

            if continue_voting.lower() == "no":
                break

            print("-------------------------------------")

    else:
        # Voter is below 18 years old
        print("Sorry! You are not eligible to vote.")
        print("You must be 18 or above.")
        exit()


# ================= VOTING RESULT =================

# Ask whether the user wants to see the result
show_result = input(
    "Do you want to see the result? (yes/no): "
)

if show_result.lower() == "yes":

    print("=====================================")
    print("          VOTING RESULT")
    print("=====================================")

    # Display the total votes received by each candidate
    print(f"Rahul : {ll['Rahul']} votes")
    print(f"Amit  : {ll['Amit']} votes")
    print(f"Priya : {ll['Priya']} votes")
    print(f"NOTA  : {ll['NOTA']} votes")

    print("=====================================")

    # Find the maximum number of votes
    max_votes = max(ll.values())

    # Find all candidates who received the maximum votes
    winners = [
        candidate
        for candidate, votes in ll.items()
        if votes == max_votes
    ]

    # Check whether there is a tie
    if len(winners) > 1:
        print("ELECTION TIE")
        print("Candidates:", winners)
        print("Votes:", max_votes)

    else:
        print("WINNER:", winners[0])
        print("Votes:", max_votes)

else:
    print("Thank you!")

