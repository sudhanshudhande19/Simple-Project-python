name =input("Enter The Student Nmame  =") #Input The Student Name 
rollno = int(input("Enter the Roll No =")) #Input The  Student Roll Number 

subjectMarks = int(input("Enter The Python Subject Mark  =")) # Input The  Total Subject Marks 
subjectMarks1 =int(input("Enter The Java   Subject Mark  ="))
subjectMarks2 =int(input("Enter The SQL    Subject Mark  ="))
subjectMarks3 =int(input("Enter The PHP    Subject Mark  ="))
subjectMarks4 =int(input("Enter The DBMS   Subject Mark  ="))

if (subjectMarks > 100 or   # Check If Condition  Marks is Valid Or Not Valid 
    subjectMarks1 > 100 or
    subjectMarks2 > 100 or
    subjectMarks3 > 100 or
    subjectMarks4 > 100):
    print("Not Valid Marks")
    exit() 

elif (subjectMarks < 35 or   # Check If Condition  Marks is  Fail
    subjectMarks1 < 35 or
    subjectMarks2 < 35 or
    subjectMarks3 < 35 or
    subjectMarks4 < 35):
    print("Below 35 marks in one or more subjects.")
    print("Result = Fail")
    print("Percentage cannot be calculated.")
    exit() 




total_Marks =subjectMarks + subjectMarks1 + subjectMarks2 + subjectMarks3 + subjectMarks4 # Sum Of The Total Marks

Percentage  = (total_Marks / 500)*100    # Calculate The Percentage Of Total Marks Of Suject

print("=============================================================")

print("Name =",   name) # Print The Name , Roll No , Total Marks , Percentag
print("Roll No =",rollno)
print("Total Marks  =",total_Marks)
print("Percentage = ", Percentage)

if  Percentage >= 80  and Percentage <=100:  # check The If Condition Percentage wise Show The Grade And Result
    print("Grade  = A")
    print("Result = Pass")
elif Percentage >= 70 and Percentage < 80:
    print("Grade  = B")
    print("Result = Pass")
elif Percentage >= 50 and Percentage < 70:
    print("Grade  = C")
    print("Result = Pass")
elif  Percentage >= 40 and Percentage < 50:
    print("Grade  =  D")
    print("Result = Pass")
else:
    print("Result = Fail")