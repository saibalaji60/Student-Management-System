'''
    Author : Naga Suresh Kalla
    Date : 11-29-2023
'''

def display_welcome_page_file(filename):
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print("The file was not found.")


def replace_text_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        modified_content = file_content.replace(old_text, new_text)
        with open(file_path, 'w') as file:
            file.write(modified_content)
    except FileNotFoundError:
        pass
