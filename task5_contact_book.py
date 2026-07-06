# TASK 5 - CONTACT BOOK
# A simple contact book where the user can add, view,
# search, update, and delete contacts.

contacts = []

def show_menu():
    print("\n----- CONTACT BOOK MENU -----")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("\nNo contacts saved yet.")
        return
    print("\n--- Contact List ---")
    for i in range(len(contacts)):
        c = contacts[i]
        print(str(i + 1) + ". " + c["name"] + " - " + c["phone"])

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword in c["phone"]:
            print("\nName:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    choice = int(input("Enter the contact number to update: "))
    if 1 <= choice <= len(contacts):
        c = contacts[choice - 1]
        print("Leave a field blank to keep it unchanged.")

        new_name = input("New name (" + c["name"] + "): ")
        new_phone = input("New phone (" + c["phone"] + "): ")
        new_email = input("New email (" + c["email"] + "): ")
        new_address = input("New address (" + c["address"] + "): ")

        if new_name != "":
            c["name"] = new_name
        if new_phone != "":
            c["phone"] = new_phone
        if new_email != "":
            c["email"] = new_email
        if new_address != "":
            c["address"] = new_address

        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    choice = int(input("Enter the contact number to delete: "))
    if 1 <= choice <= len(contacts):
        removed = contacts.pop(choice - 1)
        print("Deleted contact:", removed["name"])
    else:
        print("Invalid contact number.")

# Main program loop
while True:
    show_menu()
    option = input("Choose an option (1-6): ")

    if option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        update_contact()
    elif option == "5":
        delete_contact()
    elif option == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
