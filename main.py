'''
    Author : Naga Suresh Kalla
    Date : 11-29-2023
'''


from welcome import display_welcome_page_file
from StudentManagementSystem import StudentManagementSystem
from Utilities import exit_system


def main_page():
    # Menu loop
    display_welcome_page_file("Team_Members")
    while True:

        display_welcome_page_file("welcome.txt")
        choice = 0
        try:
            choice = input("Please select (1 - 3): ")
        except KeyboardInterrupt as e:
            exit_system()
        if choice == '1':
            obj = StudentManagementSystem()
            obj.login()
            display_welcome_page_file("end.txt")

        elif choice == '2':
            obj = StudentManagementSystem()
            obj.register_user()
            display_welcome_page_file("end.txt")

        elif choice == '3':
            exit_system()

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == '__main__':
    main_page()
