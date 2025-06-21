# 📁 Contact Book using File Handling

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact saved!\n")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            print("📇 All Contacts:")
            for line in file:
                name, phone, email = line.strip().split(",")
                print(f"👤 Name: {name}, 📞 Phone: {phone}, 📧 Email: {email}")
    except FileNotFoundError:
        print("❌ No contacts found. Add some first!\n")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if search_name in name.lower():
                    print(f"🔍 Found -> Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
    except FileNotFoundError:
        print("❌ File not found.")

    if not found:
        print("🙁 Contact not found.\n")

def delete_all_contacts():
    confirm = input("Are you sure you want to delete all contacts? (yes/no): ")
    if confirm.lower() == "yes":
        open("contacts.txt", "w").close()
        print("🗑️ All contacts deleted.")
    else:
        print("Cancelled.")

def menu():
    while True:
        print("\n📱 CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_all_contacts()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
menu()
