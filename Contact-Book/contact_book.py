print("=== Contact Book ===")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Update Contact")
print("5. Delete Contact")
print("6. Exit")
print("====================")

my_list = []

while True:
    cc = int(input("Choose The Option = "))

    # New Contact Dictionary
    def tt(ll):
        ll = {
            'Enter Name': '',
            'Enter Phone': '',
            'Enter Email': ''
        }
        return ll

    kk = tt('ll')

    # ------------------ Add Contact ------------------
    if cc == 1:
        aa = input("Enter Name : ")

        pp = input("Enter Phone : ")

        # Phone number validation
        if len(pp) > 10 or len(pp) < 10:
            print("Invalid Number\n")
            continue

        ee = input("Enter Email : ")

        kk['Enter Name'] = aa
        kk['Enter Phone'] = pp
        kk['Enter Email'] = ee

        my_list.append(kk)

        print("Contact Added Successfully!\n")

    # ------------------ View Contacts ------------------
    elif cc == 2:
        if len(my_list) == 0:
            print("No Contacts Added\n")
        else:
            for i in my_list:
                print("Name  :", i["Enter Name"])
                print("Phone :", i["Enter Phone"])
                print("Email :", i["Enter Email"])
                print("--------------------")

            print("Contact View Successfully!\n")

    # ------------------ Search Contact ------------------
    elif cc == 3:
        name = input("Enter Name to Search : ")

        for i in my_list:
            if i["Enter Name"] == name:
                print("Name  :", i["Enter Name"])
                print("Phone :", i["Enter Phone"])
                print("Email :", i["Enter Email"])
                print("Contact Search Successfully!")
                print("--------------------\n")
                break
        else:
            print("Contact Not Found!\n")

    # ------------------ Update Contact ------------------
    elif cc == 4:
        name2 = input("Enter Contact Name To Update : ")

        for i in my_list:
            if i["Enter Name"] == name2:

                pp1 = input("Enter New Phone No : ")

                if len(pp1) > 10 or len(pp1) < 10:
                    print("Invalid Number\n")
                    break

                ee1 = input("Enter New Email : ")

                # Update Contact
                i["Enter Phone"] = pp1
                i["Enter Email"] = ee1

                print("Name  :", i["Enter Name"])
                print("Phone :", i["Enter Phone"])
                print("Email :", i["Enter Email"])
                print("Contact Updated Successfully!")
                print("--------------------\n")
                break
        else:
            print("Contact Not Found!\n")

    # ------------------ Delete Contact ------------------
    elif cc == 5:
        delete = input("Enter Contact Name To Delete : ")

        for i in my_list:
            if i["Enter Name"] == delete:

                print("Name  :", i["Enter Name"])
                print("Phone :", i["Enter Phone"])
                print("Email :", i["Enter Email"])

                # Remove Contact
                my_list.remove(i)

                print("Contact Deleted Successfully!")
                print("--------------------\n")
                break
        else:
            print("Contact Not Found!\n")

    # ------------------ Exit ------------------
    elif cc == 6:
        print("Exit Successfully!")
        break

    # ------------------ Invalid Option ------------------
    else:
        print("Invalid Option\n")