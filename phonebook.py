# this code note downs the  values in an phonebook

def display_phonebook(phonebook):
    """Displays the current entries in the phonebook."""
    if phonebook:
        print("\nCurrent Phonebook:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("\nThe phonebook is empty.")

def add_entry(phonebook):
    """Adds a new entry to the phonebook."""
    name = input("Enter the name: ").strip()
    if name in phonebook:
        print(f"{name} is already in the phonebook. Use the update option to change the number.")
    else:
        number = input(f"Enter the phone number for {name}: ").strip()
        phonebook[name] = number
        print(f"Added {name} to the phonebook.")

def update_entry(phonebook):
    """Updates an existing entry in the phonebook."""
    name = input("Enter the name to update: ").strip()
    if name in phonebook:
        number = input(f"Enter the new phone number for {name}: ").strip()
        phonebook[name] = number
        print(f"Updated {name}'s phone number.")
    else:
        print(f"{name} is not in the phonebook.")

def delete_entry(phonebook):
    """Deletes an entry from the phonebook."""
    name = input("Enter the name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name} from the phonebook.")
    else:
        print(f"{name} is not in the phonebook.")

def main():
    """Main function to manage the phonebook."""
    phonebook = {}
    while True:
        print("\nPhonebook Menu:")
        print("1. Add an Entry")
        print("2. Update an Entry")
        print("3. Delete an Entry")
        print("4. Display Phonebook")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            update_entry(phonebook)
        elif choice == "3":
            delete_entry(phonebook)
        elif choice == "4":
            display_phonebook(phonebook)
        elif choice == "5":
            print("Exiting the phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
