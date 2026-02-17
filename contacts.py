# Simple To-Do List Program
# Created for CodSoft Python Programming Internship
# Author: Revathi R

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = [phone, email, address]
        print("Contact added successfully")

    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            for name, details in contacts.items():
                print("Name:", name, "| Phone:", details[0])

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            details = contacts[search]
            print("Phone:", details[0])
            print("Email:", details[1])
            print("Address:", details[2])
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name] = [phone, email, address]
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == "6":
        print("Exiting Contact Book")
        break

    else:
        print("Invalid choice")