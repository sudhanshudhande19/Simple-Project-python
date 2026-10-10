
# -----------------------------------------------
# MOVIE COLLECTION MANAGER
# -----------------------------------------------

my_list_movies = []


def add_movie():
    movie = {
        'MovieID': int(input("Enter Movie ID: ")),
        'MovieName': input("Enter Movie Name: "),
        'ReleaseYear': int(input("Enter Release Year: ")),
        'Genre': input("Enter Genre: "),
        'Language': input("Enter Language: "),
        'Director': input("Enter Director Name: "),
        'IMDbRating': float(input("Enter IMDb Rating: ")),
        'YourRating': float(input("Enter Your Rating: ")),
        'watchedit?': input("Have you watched it? (yes/no): ").lower(),
        'favourite?': input("Is it your favourite? (yes/no): ").lower()
    }

    my_list_movies.append(movie)
    print("Movie added successfully!")


def view_movies():
    print("\n========== ALL MOVIES ==========")

    if len(my_list_movies) == 0:
        print("No movies added yet!")
        return

    for i in my_list_movies:
        print("-----------------------------------")
        print("Movie ID     :", i['MovieID'])
        print("Movie Name   :", i['MovieName'])
        print("Release Year :", i['ReleaseYear'])
        print("Genre        :", i['Genre'])
        print("Language     :", i['Language'])
        print("Director     :", i['Director'])
        print("IMDb Rating  :", i['IMDbRating'])
        print("Your Rating  :", i['YourRating'])
        print("Watched      :", i['watchedit?'])
        print("Favourite    :", i['favourite?'])

    print("-----------------------------------")
    print("Total Movies:", len(my_list_movies))


def search_movie():
    movie_id = int(input("Enter Movie ID to search: "))

    for i in my_list_movies:
        if i['MovieID'] == movie_id:
            print("\nMovie Found!")
            print("Movie Name  :", i['MovieName'])
            print("Release Year:", i['ReleaseYear'])
            print("Genre       :", i['Genre'])
            print("Your Rating :", i['YourRating'])
            print("Watched     :", i['watchedit?'])
            print("Favourite   :", i['favourite?'])
            return

    print("Movie not found!")


def update_movie():
    movie_id = int(input("Enter Movie ID to update: "))

    for i in my_list_movies:
        if i['MovieID'] == movie_id:
            print("Movie Found:", i['MovieName'])

            print("\n1. Movie Name")
            print("2. Release Year")
            print("3. Genre")
            print("4. Language")
            print("5. Director Name")
            print("6. IMDb Rating")
            print("7. Your Rating")
            print("8. Watched Status")
            print("9. Favourite Status")

            choice = int(input("What do you want to update? "))

            if choice == 1:
                i['MovieName'] = input("Enter New Movie Name: ")

            elif choice == 2:
                i['ReleaseYear'] = int(input("Enter New Release Year: "))

            elif choice == 3:
                i['Genre'] = input("Enter New Genre: ")

            elif choice == 4:
                i['Language'] = input("Enter New Language: ")

            elif choice == 5:
                i['Director'] = input("Enter New Director Name: ")

            elif choice == 6:
                i['IMDbRating'] = float(input("Enter New IMDb Rating: "))

            elif choice == 7:
                i['YourRating'] = float(input("Enter New Your Rating: "))

            elif choice == 8:
                i['watchedit?'] = input("Watched? (yes/no): ").lower()

            elif choice == 9:
                i['favourite?'] = input("Favourite? (yes/no): ").lower()

            else:
                print("Invalid update choice!")
                return

            print("Movie details updated successfully!")
            return

    print("Movie not found!")


def delete_movie():
    movie_id = int(input("Enter Movie ID to delete: "))

    for i in my_list_movies:
        if i['MovieID'] == movie_id:
            confirm = input(
                "Are you sure you want to delete this movie? (yes/no): "
            ).lower()

            if confirm == 'yes':
                my_list_movies.remove(i)
                print("Movie deleted successfully!")
            else:
                print("Delete cancelled!")

            return

    print("Movie not found!")


def show_favourite_movies():
    print("\n========== FAVOURITE MOVIES ==========")
    found = False

    for i in my_list_movies:
        if i['favourite?'] == 'yes':
            print(i['MovieName'], "| Rating:", i['YourRating'])
            found = True

    if not found:
        print("No favourite movies found!")


def show_watched_movies():
    print("\n========== WATCHED MOVIES ==========")
    found = False

    for i in my_list_movies:
        if i['watchedit?'] == 'yes':
            print(i['MovieName'], "| Year:", i['ReleaseYear'])
            found = True

    if not found:
        print("No watched movies found!")


while True:
    print("\n========== MOVIE COLLECTION MANAGER ==========")
    print("1. Add Movie")
    print("2. View All Movies")
    print("3. Search Movie")
    print("4. Update Movie")
    print("5. Delete Movie")
    print("6. Show Favourite Movies")
    print("7. Show Watched Movies")
    print("8. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        add_movie()

    elif option == '2':
        view_movies()

    elif option == '3':
        search_movie()

    elif option == '4':
        update_movie()

    elif option == '5':
        delete_movie()

    elif option == '6':
        show_favourite_movies()

    elif option == '7':
        show_watched_movies()

    elif option == '8':
        print('==============================================')
        print("Thank you for using Movie Collection Manager!")
        print("Program closed successfully.")
        print('==============================================')
        break

    else:
        print("Invalid choice! Please enter 1 to 8.")
        
