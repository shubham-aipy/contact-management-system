import json
contact = {}


def load_contacts():
    try:
        with open("contacts.json") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def show_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contact:
        print("contact is already saved!")
    else:
        phone = input("Enter contact phone: ").strip()
        email = input("Enter email(Optional): ").strip()
        contact[name] = {"name": name, "phone": phone, "email": email}
        show_contacts(contact)
        print(f'Contact {name} added!')


def search_contact():
    name = input("Enter Contact name: ").strip()
    if name in contact:
        print(f' Name: {name}')
        print(f' Phone: {contact[name]["phone"]}')
        print(f' E mail: {contact[name]["email"]}')
    else:
        print("contact not found!")


def update_contact():
    name = input("Enter contact name for Update: ").strip()
    if name in contact:
        phone = input("Enter Updated contact phone: ").strip()
        email = input("Enter Updated email(Optional): ").strip()
        contact[name] = {"phone": phone, "email": email}
        show_contacts(contact)
        print(f'Contact {name} Updated!')
        return contact[name]
    return None


def delete_contact():
    name = input("Enter contact name for delete: ").strip()
    if name in contact:
        delete = input("Delect Contact? (y/n):").strip().lower()
        if delete == "y":
            del contact[name]
            print(f'Contact {name} Deleted Successfully!')
    else:
        print("Contact not found!")

def view_all_contacts():
    if contact:
        print("All Contacts:")
        for name, info in contact.items():
            print(f'Name: {name}')
            print(f'Phone: {info["phone"]}')
            print(f'Email: {info["email"]}')
    else:
        print("Contact Folder is empty")


while True:
    print(" ===Contact Numbers=== ")
    print("1. Add Contacts")
    print("2. Search Contacts")
    print("3. Update Contacts")
    print("4. Delete Contacts")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice? (1/6): ").strip().lower()
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        view_all_contacts()
    elif choice == "6":
        break

    else:
        print("invalid choice! Try again")


