'''
    Author : Naga Suresh Kalla
    Date : 11-29-2023
'''

from Utilities import password_check, name_check, username_check, login_username_check, verify_password
from Database import Session
from welcome import display_welcome_page_file, replace_text_in_file
from CURD import add_user, get_all_users, get_password_of_user
from Account import account_operations


class StudentManagementSystem:

    def login(self):
        session = Session()
        print("=====================Login======================")

        while True:
            username_input = input("Please Enter Your Account: ")

            # Check if the username is valid
            if login_username_check(username_input, get_all_users(session), "✖ Login Failed! Account Not Exists"):
                break

        while True:
            password_input = input("Enter your password: ")
            # Check if the password is correct
            if verify_password(get_password_of_user(username_input, session=session), password_input):
                break
            else:
                print("✖ Login Failed! Invalid Password")

        account_operations(username_input)
        session.close()

    def register_user(self):
        session = Session()
        display_welcome_page_file("register.txt")
        while True:
            username = input("Please Enter Account Name: ")
            if not name_check(username):
                continue
            if not username_check(username, get_all_users(session=session),
                                  "✖ Registration Failed! Account Already Exists"):
                return
            break
        display_welcome_page_file("password.txt")
        while True:
            password = input("Enter a password: ")
            hashed_password = password_check(password)
            if not hashed_password:
                continue
            add_user(username, hashed_password, session=session)
            print("    ✔ Registration successful!  ")
            session.close()
            return
