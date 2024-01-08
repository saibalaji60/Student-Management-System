'''
    Author : Naga Suresh Kalla
    Date : 11-30-2023
'''

from welcome import display_welcome_page_file, replace_text_in_file
from Show_Student import student_views
from Add_Student import add_student, modify_student, delete_student
from Query_Score import query_score


def account_operations(username):
    if username:
        replace_text_in_file("student.txt", "%s", username)

        while True:
            try:
                display_welcome_page_file("student.txt")

                choice = input("Please select (1 - 6): ")

                if choice == '1':
                    add_student()
                elif choice == '2':
                    student_views(username)
                elif choice == '3':
                    modify_student()
                elif choice == '4':
                    delete_student()
                elif choice == '5':
                    query_score()
                elif choice == '6':
                    replace_text_in_file("student.txt", username, "%s")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")

            except:
                replace_text_in_file("student.txt", username, "%s")
                break
