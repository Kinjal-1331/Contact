contact = {}
while True:
    print("Contact Book Me Aapka Swagat Haii! ")
    print("1. Create the contact")
    print("2. Delete the contact")
    print("3. Update the contact")
    print("4. Search the contact")
    print("5. Count the contact")
    print("6. View the contact")
    print("7. Exit")

    choice = input("Enter Your choice : ")

    if choice == '1':
        name = input("Enter a Name : ")
        if name in contact:
            print(f"Contact name {name} is already exists !")
        else:
            try:
                mobile = int(input("Enter a Mobile Number : "))
                email = input("Enter a Email-id : ")
                contact[name] = {'mobile': mobile, 'email': email}
                print(f'Contact name {name} has been created...')
            except:
                print("Invalid mobile number..!")

    elif choice == '2':
        name = input("Enter a name Which You delete in Contact Book : ")
        if name in contact:
            print(f"Contact name {name} has been Deleted...")
            del contact[name]
        else:
            print(f"Contact Name {name} has not Found...")

    elif choice == '3':
        name = input("Enter a name for update : ")
        if name in contact:
            updated_name = input("Enter a Updated Name : ")
            try:
                mobile = int(input("Enter a updated Mobile Number : "))
                email = input("Enter a updated Email-id : ")
                
                contact[updated_name] = {'mobile': mobile, 'email': email}
                del contact[name]
            except:
                print("Invalid mobile number..!")
        else:
            print(f"Contact Name {name} is Not found")

    elif choice == '4':
        name = input("Enter a name to search it is present or not in Contact Book !: ")
        if name in contact:
            print(f'Contact name {name} is a Present in Contact Book...')
        else:
            print(f"Contact Name {name} is not present in Contact Book...")

    elif choice == '5':
        count = 0
        for i in contact:
            count += 1
        print(f"There Are {count} Contacts In Contacts Book...")

    elif choice == '6':
        name = input("Enter a name to see his/her Details: ")
        if name in contact:
            print(f"Name : {name}")
            print(f"Mobile Number : {contact[name]['mobile']}")
            print(f"Email-id: {contact[name]['email']}")
        else:
            print(f"Contact Name {name} is not found")

    elif choice == '7':
        print("Thank You...!")

    else:
        print("Invalid Choice...")

