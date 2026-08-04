# ==============================
# Student Record Management System
# ==============================

# Display Main Menu
print("========Student Record System========") 
print("1. Add Student")
print("2. View Student")
print("3. Search Student")
print("4. Update Student")
print("5. Calculate Grade")                      
print("6. Delete Student")                        
print("7. Save to File")
print("8. Exit")
print("=====================================")

# List to store all student records
my_student_record = []   

# Program runs until user chooses Exit
while True:

    # Function to create an empty student dictionary
    def sudhanshu(student_record):               
        student_record = {
            "student_id": " ",
            "name": " ",
            "Roll no": " ",
            "age": " ",
            "gender": " ",
            "branch": " ",
            "year": " ",
            "section": " ",
            "mobile_no": " ",
            "email": " ",
        }
        return student_record

    kk = sudhanshu({})

    select_no = int(input("Enter Select The Number 1 to 8 ="))

    if select_no == 1:
        # -----------------------------
        # Option 1 : Add Student Record
        # -----------------------------
        print("=======Add Student Record=======")
        student_id = int(input("Enter Student ID ="))
        student_name = input("Enter The Student Name  =")
        student_rollno = int(input("Enter The Student Roll No ="))
        student_age = int(input("Enter The Student Age = "))          
        student_gender = input("Enter The Student Gender = ")          
        student_branch = input("Enter The Student Branch = ")
        student_year = input("Enter The Student Year = ")
        student_section = input("Enter The Student Section = ")
        student_mobile_no = input("Enter The Student Mobile No = ")
        if len(student_mobile_no) != 10:
            print("Enter The Valid Mobile No")
        student_email = input("Enter The Student Email = ")

        kk["student_id"] = student_id
        kk["name"] = student_name
        kk["Roll no"] = student_rollno
        kk["age"] = student_age
        kk["gender"] = student_gender
        kk["branch"] = student_branch
        kk["year"] = student_year
        kk["section"] = student_section
        kk["mobile_no"] = student_mobile_no
        kk["email"] = student_email

        mark = int(input("How Many Subject You Have ="))


        for i in range(1, mark + 1):
            subject_name = input("Enter The Subject Name = ")
            subject_mark = int(input("Enter The Subject Mark ="))     
            kk["subject_name"] = subject_name
            kk["subject_marks"] = subject_mark                        
        my_student_record.append(kk)
        print("Student Information Added Successfully!")
        print("========================================")
        print()
        
    # -----------------------------
    # Option 2 : View Student Record
    # -----------------------------
    elif select_no == 2:

        print("=====View Student Information======")
        if len(my_student_record) == 0:
            print("No Student Record Found")          
            print("================================")

        else:
            for i in my_student_record:
                print("Student ID     =", i["student_id"])
                print("Student Name   =", i["name"])
                print("Roll No        =", i["Roll no"])
                print("Age            =", i["age"])
                print("Gender         =", i["gender"])         
                print("Branch         =", i["branch"])
                print("Year           =", i["year"])
                print("Section        =", i["section"])
                print("Mobile No      =", i["mobile_no"])
                print("Email          = ", i["email"])
                print("Subject Name   =", i["subject_name"])
                print("Subject Marks  =", i["subject_marks"])  
                print()
                print("View Student Record Successfully!")
                print("================================")
                print()
                
    # -----------------------------
    # Option 3 : Search Student
    # -----------------------------
    elif select_no == 3:

        print("=======Search Student Record=======")
        name = input("Enter The Student Name  = ")
        found = False                                    
        for i in my_student_record:
            if i["name"] == name:
                found = True
                print("Student Name   =", i["name"])
                print("Student ID     =", i["student_id"])
                print("Roll No        =", i["Roll no"])
                print("Age            =", i["age"])
                print("Gender         =", i["gender"])
                print("Branch         =", i["branch"])
                print("Year           =", i["year"])
                print("Section        =", i["section"])
                print("Mobile No      =", i["mobile_no"])
                print("Email          = ", i["email"])
                print("Subject Name   =", i["subject_name"])
                print("Subject Marks  =", i["subject_marks"])
                print()
                print("Search Student Record Successfully!")
                print("================================")
                print()

        if not found:
            print("Student Record Not Found")
            print("================================")
            print()
            
    # -----------------------------
    # Option 4 : Update Student Record
    # -----------------------------
    elif select_no == 4:
        print("=======Updated Student Record========")
        roll_no = int(input("Enter The Student Roll No ="))
        found = False                                    
        
                                                           
        for i in my_student_record:
            kk = i
            if i["Roll no"] == roll_no:
                found = True
                S_name = input("Enter The Updated Student Name = ")
                S_age = int(input("Enter The updated Student Age ="))
                S_branch = input("Enter The Updated Student Branch Name")
                S_section = input("Enter The Updated Student Section = ")
                S_mobilno = input("Enter The Updated Student Mobile No =")
                if len(S_mobilno) != 10:
                    print("Enter The Valid Mobile No")
                S_email = input("Enter The Updated Student Email =")

                kk["name"] = S_name
                kk["age"] = S_age
                kk["branch"] = S_branch
                kk["section"] = S_section
                kk["mobile_no"] = S_mobilno
                kk["email"] = S_email

                for j in my_student_record:
                    print("Roll No        =", j["Roll no"])
                    print("Student Name   =", j["name"])
                    print("Age            =", j["age"])
                    print("Branch         =", j["branch"])
                    print("Section        =", j["section"])
                    print("Mobile No      =", j["mobile_no"])
                    print("Email          = ", j["email"])
                    print()
                print("Updated Student Record Successfully!")   
                print("================================")
                print()

        if not found:
            print("Not Found Student Roll Number ")
            print("================================")
            print()
    
    # -----------------------------
    # Option 5 : Calculate Grade
    # -----------------------------
    elif select_no == 5:
        print("==========Calculate Student Grade===========")
        RollNo = int(input("Enter The Student Roll No ="))
        found = False                                   
        for i in my_student_record:
            if i["Roll no"] == RollNo:
                found = True
                print("Name ", i["name"])
                print()
                print("Marks .")
                print(i["subject_name"], "=", i["subject_marks"])  
                print()
                print("---------------------------------------------------")
                Total_Marks = i["subject_marks"]
                percentage = (i["subject_marks"] / 100) * 100       
                print("Total Marks =", Total_Marks)
                print("Percentage =", percentage)
                if percentage >= 90:
                    print("Grade = A")
                elif percentage >= 80:
                    print("Grade = B")
                elif percentage >= 70:
                    print("Grade = C")
                elif percentage >= 60:
                    print("Grade = D")
                elif percentage >= 40:
                    print("Grade = E")
                else:
                    print("Grade = Fail(F)")
                print("---------------------------------------------------")
                print("Calculate Student Grade Successfully!")
                print("=====================================================")
                print()

        if not found:
            print("Student Record Not Found")
            print("=====================================================")
            print()
            
    # -----------------------------
    # Option 6 : Delete Student Record
    # -----------------------------
    elif select_no == 6:
        print("==========Delete Student Record========")
        rollno = int(input("Enter The Student Roll No ="))
        found = False                                   
        for i in my_student_record:
            if i["Roll no"] == rollno:
                found = True

                
                confirm = input("Are You Sure You Want To Delete Student Record (Yes/No) =")
                if confirm == 'Yes' or confirm == 'yes':
                    my_student_record.remove(i)
                    print("Student Record Deleted Successfully!")   
                    print("====================================")
                    print()
                else:
                    print("Student Record Not Deleted")
                break   

        
        if not found:
            print("Student Roll No Not Found ")
            print("=======================================")
            print()
            
    # -----------------------------
    # Option 7 : Save Records to File
    # -----------------------------
    elif select_no == 7:
        print("========== Save To File ==========")

        if len(my_student_record) == 0:
            print("No Student Record Found!")
            print()
        else:
            file = open("student_record.txt", "w")

            for i in my_student_record:
                file.write(f"Student ID : {i['student_id']}\n")
                file.write(f"Name : {i['name']}\n")
                file.write(f"Roll No : {i['Roll no']}\n")
                file.write(f"Age : {i['age']}\n")
                file.write(f"Gender : {i['gender']}\n")
                file.write(f"Branch : {i['branch']}\n")
                file.write(f"Year : {i['year']}\n")
                file.write(f"Section : {i['section']}\n")
                file.write(f"Mobile No : {i['mobile_no']}\n")
                file.write(f"Email : {i['email']}\n")

                file.write("------------------------------\n")

            file.close()

            print("Student Records Saved Successfully!")
            print("File Name : student_record.txt")
            print("===================================")
            print()
    # -----------------------------
    # Option 8 : Exit Program
    # -----------------------------
    elif select_no == 8:
        print("Exiting the Student Record System. Goodbye!")
        break