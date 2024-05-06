from utils import load_notes, add_note, delete_note, display_notes, edit_note, NOTES_FILE
import os

def main():
    while True:
        print("\nMenu:")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            notes = load_notes()
            if notes:
                display_notes(notes)
            else:
                print("No notes found.")
        elif choice == "2":
            add_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as file:
            file.write("[\n]")
    main()