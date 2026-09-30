# ======================= EMPLOYEE SALARY DETAILS =======================

my_list_emp = []


# Function to create an employee dictionary
def EMP():
    my_dict_emp = {
        'Employee ID': '',
        'Employee Name': '',
        'Department': '',
        'Net Salary': ''
    }
    return my_dict_emp


while True:

    # Ask the user whether they want to check employee salary details
    check = input("Check the Employee Salary Details (yes/no) = ").lower()

    if check == 'yes':

        print('\n========== EMPLOYEE SALARY DETAILS ==========')

        # Take employee information
        employee_id = int(input("Employee ID    : "))
        employee_name = input("Employee Name  : ")
        department = input("Department     : ")

        # Take salary information
        basic_salary = int(input("Basic Salary   : "))
        hra = int(input("HRA            : "))
        da = int(input("DA             : "))
        ta = int(input("TA             : "))
        bonus = int(input("Bonus          : "))

        # Calculate Gross Salary
        gross_salary = basic_salary + hra + da + ta + bonus

        # Take deduction information
        pf = int(input("PF             : "))
        tax = int(input("Tax            : "))

        # Calculate Total Deduction
        total_deduction = pf + tax

        # Calculate Net Salary
        net_salary = gross_salary - total_deduction

        # Create a new dictionary for every employee
        my_fun = EMP()

        # Store employee details in dictionary
        my_fun['Employee ID'] = employee_id
        my_fun['Employee Name'] = employee_name
        my_fun['Department'] = department
        my_fun['Net Salary'] = net_salary

        # Add employee dictionary to the list
        my_list_emp.append(my_fun)

        # Display Employee Salary Details
        print('\n========== EMPLOYEE SALARY DETAILS ==========')

        print('Employee ID     =', employee_id)
        print('Employee Name   =', employee_name)
        print('Department      =', department)

        print('Basic Salary    =', basic_salary)
        print('HRA             =', hra)
        print('DA              =', da)
        print('TA              =', ta)
        print('Bonus           =', bonus)

        print()

        print('Gross Salary    =', gross_salary)

        print()

        print('PF              =', pf)
        print('Tax             =', tax)
        print('Total Deduction =', total_deduction)

        print()

        print('-----------------------------------------')
        print('Net Salary      =', net_salary)
        print('=========================================')

    elif check == 'no':
        print("Thank you!")
        break

    else:
        print("Please enter only yes or no.")

