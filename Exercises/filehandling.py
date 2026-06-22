# This program allows users to save and read notes using file handling in Python.\
# The notes are stored in a text file called "notes.txt". 
# Users can choose to save a new note, read all existing notes, or exit the program.
# The program uses functions to handle saving and loading notes, as well as displaying options to the user. 
# It continues to run until the user chooses to exit.

def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(f"{note}\n")

def load_notes():
    try:
        notes = []
        
        with open("notes.txt", "r") as file:
            for line in file:
                note = line.strip()
                notes.append(note)

        return notes
    except FileNotFoundError:
        return 'No notes found. Please save a note first.'

def count_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        return len(notes)

    except FileNotFoundError:
        return 0
    
def options():
    print("Options:")
    print("1. Save Note")
    print("2. Read Notes")
    print("3. Notes Count")
    print("4. Exit")
    return input("Choose an option: ")

def main():
    while True:
        choice = options()
        if choice == '1':
            note = input("Enter a note to save:\n")
            save_note(note)
            print("Note saved successfully!")

        elif choice == '2':
            notes = load_notes()

            if isinstance(notes, str):
                print(notes)

            else:
                for note in notes:
                    print(note)
        elif choice == '3':
            print(f"Total notes: {count_notes()}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.") 

if __name__ == "__main__":    main()
