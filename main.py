import os

if not os.path.exists("contacts"):
    os.mkdir("contacts")


def addContact():
    name = input("Enter the name of the contact\n")
    phone = input("Enter the phone number of the contact\n")

    # Check for a valid phone number
    if len(phone) < 9:
        print("Phone number should be 10 digits")
        return
    email = input("Enter the email of the contact\n")

    # Check for a valid email
    if email.count("@") == 0:
        print("Your email does not appear to be valid")
        return

    # Check if the phone number already exists
    with open("contacts/contacts.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            details = line.split(",")
            if name.lower().strip() == details[0].lower().strip():
                print("Contact already exists")
                return

    # Add the new contact
    with open("contacts/contacts.txt", "a") as f:
        f.write(f"{name}, {phone}, {email}\n")


def viewContacts():
    # Open the contacts file and read the contact information and print the contact information
    with open("contacts/contacts.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            details = line.split(",")
            email = details[2].replace("\n", " ")
            print(f"{details[0]}, {details[1]}, {email}")


def searchContact():
    # Search for a contact
    name = input("Write the name of the contact").lower().strip()
    with open("contacts/contacts.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            details = line.split(",")
            if name == details[0].lower().strip():
                print("Contact Found!")
                print(f"{details[0]}, {details[1]}, {details[2]}")


while True:
    try:
        userInput = int(input("\nWrite 1 to add a new contact\nWrite 2 to view contacts\nWrite 3 to search for contacts\n"))
    except ValueError:
        print("Please enter a number")
        break

    if userInput == 1:
        addContact()
    elif userInput == 2:
        viewContacts()
    elif userInput == 3:
        searchContact()
    else:
        print("Please enter a number from the above options!")

# By Aditya Raj
