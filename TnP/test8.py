#create a contact dictionary to read number and name from user and add to contact

contact={}
while True:
    
    print("1. Add ")
    print("2. Seacrh ")
    print("3. Display ")
    print("0. Exit ")

    ch=(input(":"))
    if ch=='1':
        name=input("Enter Name:")
        Number=int(input("Enter Number:"))

        if(len(str(Number))!=10):
            print("Number should be of 10 digit")
            continue

        contact[Number]=name
        print("Contact Added...")
    elif ch=='2':
        Number=int(input("Enter Number:"))
        if(len(str(Number))!=10):
            print("Number should be of 10 digit")
            continue

        if Number in contact:
            print(f"{Number} is of {contact[Number]}")
        else:
            print(f"{Number} is not there")

    elif ch=='0':
        print("thanks")
        break

    elif ch=='3':
        print(contact)

    else:
        print("Wrong input, try again")