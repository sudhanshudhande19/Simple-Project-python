print("=====Library Management System=====")

print("1.  Add Book")
print("2.  View Book")
print("3.  Search Book")
print("4.  Issue Book")
print("5.  Return Book")
print("6.  Delete Book")
print("7.  Exit")

print("====================================")
# Store all books
my_book = []

# Store issued book details of students
my_student =[]

# Create a new book dictionary
def system_library(book):
    book ={
                "book_id" : "",
                "book_name" : " ",
                "author_name": " ",
                "category" : " ",
                "quantity" : " "

        }
    return book

# Create a new student dictionary
def student_id (student):
    student ={
            "student_id" : "",
            "student_name" : " ",
            "mobil_no" : " ",
            "issued_book_id" : " ",
            "catagory" : " "
        }
    return student
ll = student_id({})


# Main program starts here
while True:
    Option  = int(input("Select The Opetion 1 to 7 ="))
   
    # Option 1 : Add Book
    if Option == 1:
        kk  = system_library({})

        Add_book_id  = int(input("Enter Add Book ID = "))
        Book_Name = input("Enter The Add Book Name = ")
        A_Name = input("Enter Author Name = ")
        catagory = input("Enter Book  Catagory = ")
        quantity_book = int(input("Enter The Quantity Book = "))
        kk["book_id"] =Add_book_id
        kk["book_name"] = Book_Name
        kk["authoe_name"] = A_Name
        kk["quantity"] = quantity_book
        kk["catagory"] = catagory
        my_book.append(kk)

        print("Book Add Successfully!")
        print("==============================")
        print()

    # Option 2 : View All Books
    elif Option == 2:
        if len(my_book) == 0:
            print("Book Is Not Added plese Add The Book And Then Check View Option")
        else:
            for i in my_book:
                print("Book ID :",i["book_id"])
                print("Book Name :",i["book_name"])
                print("Author  :",i["authoe_name"])
                print("Quantity :",i["quantity"])
                print("Status : Available")
                print("View All Book successfully!")
                print("===============================")
        print()

    # Option 3 : Search Book
    elif Option == 3:
        Enter_book_name = input("Enter Book Name = ")
        for i in my_book:
            if i["book_name"] == Enter_book_name:
                print(" Is Found")
                print("Book ID :",i["book_id"])
                print("Author  :",i["authoe_name"])
                print("Quantity :",i["quantity"])
                print("Status : Available")
                print("Search Book Successfully!")
                print("========================")
                print()
            else:
                print(" Book Name Is Not Found ")
                print()

    # Option 4 : Issue Book
    elif Option == 4:
        enter_book = int(input("Enter Book ID = "))
        Enter_Student = input("Enter Student Name = ")
        Enter_Student_ID = int(input("Enter Student ID = "))
        mobile_number = input("Enter Mobile Number = ")

        # Check mobile number
        if len(mobile_number) != 10:
            print("Invalid Mobile Number")
            print()
            continue

        found = False

        # Check whether book is available
        for i in my_book:
            if i["book_id"] == enter_book:
                found = True

                # Reduce quantity after issuing book
                if i["quantity"] > 0:
                    i["quantity"] -= 1

                    # Save student details
                    ll["issued_book_id"] = enter_book
                    ll["student_name"] = Enter_Student
                    ll["student_id"] = Enter_Student_ID
                    ll["mobil_no"] = mobile_number

                    my_student.append(ll)

                    print("Book Issued Successfully!")
                    print("Remaining Quantity :", i["quantity"])
                    print("================================")
                else:
                    print("Book is Out of Stock!")
                break

        else:
            print("BOOK ID DOES NOT EXIST")
            print()

    # Option 5 : Return Book
    elif Option == 5:
        
        Book_return = int(input("Enter Book ID = "))
        name = input("Enter Student Name = ")

        found = False

        for student in my_student:
            if student["issued_book_id"] == Book_return and student["student_name"] == name:

                # Increase quantity after returning book
                for book in my_book:
                    if book["book_id"] == Book_return:
                        book["quantity"] += 1
                        break

                my_student.remove(student)

                print("Book Returned Successfully!")
                print("Available Quantity :", book["quantity"])
                print("==============================")
                found = True
                break

        # Remove student record
        if not found:
            print("Book ID or Student Name Not Found")

    # Option 6 : Delete Book
    elif Option == 6:
        de_book = int(input("Enter Book ID = "))

        found = False

        for book in my_book:
            if book["book_id"] == de_book:
                my_book.remove(book)
                print("Book Deleted Successfully!")
                print("========================")
                found = True
                break

        if not found:
            print("Book ID Not Found")

    # Option 7 : Exit Program
    elif Option == 7:
        print("Thank You For Using Library Management System")
        print("================================")
        break

    else:
        print("Invalid Option")
                


