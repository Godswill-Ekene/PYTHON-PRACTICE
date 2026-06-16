#Advanced list and data stuctures
from allstudent_module import show_students
from add_module import add_student
from search_module import search_student
from menu_module import menu
def main():
    while True:
        choice = menu()

        if choice == '1':
            add_student()

        elif choice == '2':
            search_student()

        elif choice == '3':
            show_students()

        elif choice == '4':
            print('Goodbye!')
            break

        else:
            print('Invalid choice! Please try again.')

main()

    

    

    
