'''
    Author : Naga Suresh Kalla
    Date : 11-29-2023
'''

import hashlib
import re
import sys


# checks for password pattern and hashes for registration
def password_check(p):
    # Password must start with one of the following special characters !@#$%^&*
    # Must contain at least one digit, one lowercase letter, and one uppercase letter
    # Must be between 6 and 12 characters long
    if re.match(r'^(?=.*[!@#$%^&*])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,12}$', p):
        hashed_password = hashlib.md5(p.encode()).hexdigest()
        return hashed_password
    else:
        print("✖ Password Not Valid!")
        return None


def verify_password(hashed_password, password):
    # Check if the provided password matches the stored password for the username for Login
    if password:
        entered_password_hash = hashlib.md5(password.encode()).hexdigest()
        return entered_password_hash == hashed_password
    else:
        print("Verify password error")
        return False


def username_check(name, existing_usernames, message):
    # Check if the username is already taken and meets other criteria
    if name in existing_usernames:
        print(message)
        return False
    return True


def login_username_check(name, existing_usernames, message):
    if name not in existing_usernames:
        print(message)
        return False
    return True


def phone_check(phone):
    # Validate the phone number format (xxx-xxx-xxxx)
    if re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
        return True
    else:
        print(" ✖ Invalid phone number format. Please use the format xxx-xxx-xxxx.")
        return False


def name_check(name):
    # The first letter of username must be capitalized
    # username must each have at least 3 to 6 letters
    # No digit allowed in the name
    if re.match(r'^[A-Z][a-zA-Z]{2,5}$', name):
        return True
    else:
        print("✖ Account Name Not Valid!")
        return False


def age_check(age):
    # Age must be between 0 and 100
    try:
        age = int(age)
        if 0 <= age <= 100:
            return True
        else:
            print("Error: Age must be between 0 and 100.")
            return False
    except ValueError:
        print(" ✖  Invalid Age , Please use numbers")
        return False


def gender_check(gender):
    # Validate gender against a predefined set of genders
    valid_genders = ['M', 'F', 'O']
    if gender.upper() in valid_genders:
        return True
    else:
        print(" ✖ Invalid gender. Please enter M (Male), F (Female), or O (Other).")
        return False


def cus_input(current_value, message):
    # A customizable input function
    user_input = input(f"{message} (current value: {current_value}): ")
    return user_input.strip() if user_input else current_value


def exit_system():
    # Implement system exit logic
    confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
    if confirm_exit == 'y':
        print("Exiting the system. Goodbye!")
        sys.exit()
    else:
        print("Returning to the main menu.")


def verify_first_lastname_student(student, message):
    names = student.split(" ")
    if re.match(r'^[A-Z][a-zA-Z]{1,}$', names[0]) and re.match(r'^[A-Z][a-zA-Z]{1,}$', names[1]):
        return True
    else:
        print(message)
        return False


def isNotNone(sample):
    if sample is None:
        return False
    if len(sample) > 0:
        return True
    return False


def isEnteredNothing(sample):
    if len(sample) == 0:
        return True
    return False
