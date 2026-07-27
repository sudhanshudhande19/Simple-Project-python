print("===== SIMPLE CALCULATOR =====")

try:
    number = int(input("Enter The 1st Number = "))
    number2 = int(input("Enter The 2nd Number = "))

    User_operation_choose = input("Enter The Operation (+,-,*,/,%,**,//) = ")

    if User_operation_choose == "+":
        print(f"{number} + {number2} = {number + number2}")

    elif User_operation_choose == "-":
        print(f"{number} - {number2} = {number - number2}")

    elif User_operation_choose == "*":
        print(f"{number} * {number2} = {number * number2}")

    elif User_operation_choose == "/":
        if number2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"{number} / {number2} = {number / number2}")

    elif User_operation_choose == "%":
        print(f"{number} % {number2} = {number % number2}")

    elif User_operation_choose == "**":
        print(f"{number} ** {number2} = {number ** number2}")

    elif User_operation_choose == "//":
        print(f"{number} // {number2} = {number // number2}")

    else:
        print("Invalid Operator")

except ValueError:
    print("Invalid Input! Please enter only numbers.")