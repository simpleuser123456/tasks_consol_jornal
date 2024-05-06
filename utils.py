import json
from datetime import datetime
from note_model import Note

NOTES_FILE = "notes.json"

def load_notes() -> list[Note]:
    try:
        with open(NOTES_FILE, "r") as file:
            return [Note(**note_data) for note_data in json.load(file)]
    except FileNotFoundError:
        return []

def save_notes(notes: list[Note]):
    with open(NOTES_FILE, "w") as file:
        json.dump([note.dict() for note in notes], file, indent=4)

def display_notes(notes: list[Note]):
    for note in notes:
        print(f"ID: {note.id}, Title: {note.title}, Body: {note.body}, Last Modified At: {note.last_modified_at}")

def add_note():
    try:
        title = input("Enter note title: ")
        body = input("Enter note body: ")
    except KeyboardInterrupt:
        print()
        print("Exiting from add note...")
        return
    notes = load_notes()
    if notes:
        last_id = max(note.id for note in notes)
    else:
        last_id = 0
    new_note = Note(id=last_id + 1, title=title, body=body)
    notes.append(new_note)
    save_notes(notes)
    print("Note added successfully.")

def edit_note():
    try:
        note_id = int(input("Enter note ID to edit: "))
    except KeyboardInterrupt:
        print()
        print("Exiting from edit note...")
        return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    notes = load_notes()
    for note in notes:
        if note.id == note_id:
            try:
                note.title = input("Enter new title: ")
                note.body = input("Enter new body: ")
            except KeyboardInterrupt:
                print()
                print("Exiting from edit note...")
                return
            note.last_modified_at = datetime.now()
            save_notes(notes)
            print("Note edited successfully.")
            return
    print("Note not found.")

def delete_note():
    try:
        note_id = int(input("Enter note ID to delete: "))
    except KeyboardInterrupt:
        print()
        print("Exiting from delete note")
        return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    notes = load_notes()
    notes = [note for note in notes if note.id != note_id]
    save_notes(notes)
    print("Note deleted successfully.")

def display_note(notes: list[Note]):
    try:
        note_id = int(input("Enter note ID to display: "))
    except KeyboardInterrupt:
        print()
        print("Exiting from dispaly note...")
        return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    for note in notes:
        if note.id == note_id:
            print(f"ID: {note.id}, Title: {note.title}, Body: {note.body}, Last Modified At: {note.last_modified_at}")
            return
    print("Note not found.")

def display_notes_in_date_range(notes: list[Note]):
    try:
        date_start = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=0)
        date_end = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d").replace(hour=23, minute=59, second=59, microsecond=999999)

        if date_start >= date_end:
            print("Start date should be before end date.")
            return

        filtered_notes = [note for note in notes if date_start <= note.last_modified_at <= date_end]

        if filtered_notes:
            display_notes(filtered_notes)
        else:
            print("No notes found in the specified date range.")
    except KeyboardInterrupt:
        print()
        print("Exiting from displaying notes in date range...")
    except ValueError:
        print("Invalid input. Please enter dates in the format YYYY-MM-DD.")