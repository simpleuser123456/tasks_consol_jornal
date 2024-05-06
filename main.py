from utils import load_notes, add_note, delete_note, display_notes, display_note, display_notes_in_date_range, edit_note, NOTES_FILE
import os

def main():
    while True:
        print("\nMenu:")
        print("1. Display Notes")
        print("2. Display Note")
        print("3. Display Notes in date range")
        print("4. Add Note")
        print("5. Edit Note")
        print("6. Delete Note")
        print("7. Exit")
        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print()
            print("Exiting...")
            return

        if choice == "1":
            notes = load_notes()
            if notes:
                display_notes(notes)
            else:
                print("No notes found.")
        elif choice == "2":
            notes = load_notes()
            if notes:
                display_note(notes)
            else:
                print("No notes found.")
        elif choice == "3":
            notes = load_notes()
            if notes:
                display_notes_in_date_range(notes)
            else:
                print("No notes found.")
        elif choice == "4":
            add_note()
        elif choice == "5":
            edit_note()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as file:
            file.write("[\n]")
    main()