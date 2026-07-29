# INPUT THE NAME
name =input("Enter Name =")
# INPUT THE AGE
age =int(input("Enter Age ="))
# INPUT THE GENDER
gender =input("Enter  Gender=")

# INPUT THE WEIGHT AND CHECK IF CONDITION INVALID OR OVER WEIGHT
weight =int(input("Enter weight ="))
if weight <=0:
    print("Invalid Weight ")
    exit()
elif weight > 200:
    print("Over Weight ")
    exit()

# INPUT THE HEIGHT AND CHECK IF CONDTION INVALID 
height  = float(input("Enter Height  ="))
if height <=0:
    print("Invalid Height")
    exit()

#  CALCULATION AND STORE THE BMI VARIABLES
bmi = weight /( height* height )

print("--------------------------------------")

# PRINT ALL VARIABLES AND SHOW THE BMI
print("Name : ",name)
print("Age  : ",age)
print("Gender :",gender)
print("Weight : ",weight ,"kg")
print("Height : ",height,"m")
print("BMI :", round(bmi,2))

# CHECK BMI  IF CONDITION OF  3 CATEGORY

if bmi < 18.5:
    print("Category : Underweight ")
elif 18.5 <= bmi <= 24.9:
    print("Category : Normal Weight")
elif 25 <= bmi <= 29.9:
    print("Category :  Overweight")
else:
    print("Category : Obese")