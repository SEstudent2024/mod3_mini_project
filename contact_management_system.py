# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:
# Welcome to the Contact Management System! 
# Menu:
# 1. Add a new contact
# 2. Edit an existing contact
# 3. Delete a contact
# 4. Search for a contact
# 5. Display all contacts
# 6. Export contacts to a text file
# 7. Import contacts from a text file *BONUS*
# 8. Quit

import re

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes)

def validate_input(pattern, prompt):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid format. Please try again.")


# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact.
# Searching for a contact and displaying their details.
# Displaying a list of all contacts.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system. * BONUS

# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

# Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may 
# arise during execution.

def add_contact():
    name = input("Enter name: ")
    phone = validate_input(r"^\+?\d{10,15}$", "Enter phone number (10-15 digits): ")
    email = validate_input(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Enter email: ")
    address = input("Enter address (optional): ")
    notes = input("Enter any additional notes (optional): ")
    
    contacts[phone] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "notes": notes
    }
    print("Contact added successfully.")

def edit_contact():
    phone = input("Enter the phone number of the contact you want to edit: ")
    if phone in contacts:
        print("Editing contact:", contacts[phone]["name"])
        name = input("Enter new name (or press Enter to keep current): ")
        email = validate_input(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Enter new email (or press Enter to keep current): ")
        address = input("Enter new address (or press Enter to keep current): ")
        notes = input("Enter any new notes (or press Enter to keep current): ")
        
        if name: contacts[phone]["name"] = name
        if email: contacts[phone]["email"] = email
        if address: contacts[phone]["address"] = address
        if notes: contacts[phone]["notes"] = notes
        
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def search_contact():
    phone = input("Enter the phone number of the contact to search: ")
    if phone in contacts:
        print("Contact details:", contacts[phone])
    else:
        print("Contact not found.")

def display_all_contacts():
    if contacts:
        for phone, details in contacts.items():
            print(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}")
    else:
        print("No contacts available.")

def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for phone, details in contacts.items():
                file.write(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}\n")
        print("Contacts exported successfully.")
    except Exception as e:
        print("Error while exporting contacts:", e)

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                data = line.strip().split(", ")
                phone = data[0].split(": ")[1]
                contacts[phone] = {
                    "name": data[1].split(": ")[1],
                    "phone": phone,
                    "email": data[2].split(": ")[1],
                    "address": data[3].split(": ")[1],
                    "notes": data[4].split(": ")[1]
                }
        print("Contacts imported successfully.")
    except Exception as e:
        print("Error while importing contacts:", e)

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()  
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 8.")

if __name__ == "__main__":
    main()