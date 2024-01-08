'''
    Author : Naga Suresh Kalla
    Date : 11-30-2023
'''

from welcome import display_welcome_page_file
from Utilities import verify_first_lastname_student,isEnteredNothing,isNotNone, age_check, phone_check, gender_check
from Database import Session
from CURD import add_student_data,get_all_student_by_id,update_student_id,delete_student_by_id,delete_student_by_name




def add_student():
    session=Session()
    while True:
        try:
            display_welcome_page_file("add_student.txt")

            while True:
                name = input("Please Enter Student Name (Firstname Lastname): ")
                if verify_first_lastname_student(name, " ✖ Invalid Student name"):
                    break

            while True:
                age = input("Please Enter Student's Age: ")
                if age_check(age):
                    break
            while True:
                gender = input("Please Enter Student's Gender: ")
                if gender_check(gender):
                    break
            while True:
                major = input("Please Enter Student's Major: ")
                if len(major) > 0:
                    break
            while True:
                phone = input("Please Enter Student's Phone: ")
                if phone_check(phone):
                    break

            add_student_data(name, age, gender, major, phone, session)
            print("   ✔ Student Added Successfully\n ♦ 1. Continue\n ♦ 2. Exit")
            conti = input("Please Select 1 or 2: ")
            if conti != '1':
                break
        except :
            break
    session.close()
def modify_student():
    session=Session()
    id=input("Please Enter Student ID to Modify: ")
    student=get_all_student_by_id(id,session)
    if isNotNone( student):
        try:
            while True:
                age = input("New age (press enter without modification): ")
                if isEnteredNothing(str(age)):
                    age=student[0].age
                    break
                if age_check(age):
                    break
                else:
                    print(" ✖ Invalid Student Age ")
            while True:
                major = input("New Major (press enter without modification): ")
                if isEnteredNothing(major):
                    major=student[0].major
                break
            while True:
                phone = input("New phone (press enter without modification): ")
                if isEnteredNothing(phone):
                    phone=student[0].phone
                    break
                if phone_check(phone):
                    break
                else:
                    print(" ✖ Invalid Student Phone ")

            update_student_id(student[0],age,major,phone,session)
            print(" ✔ Record Modified Successfully")
        except:
            return
    else:
        print(" ✖ No Record Found ")
    session.close()

def delete_student():
    session=Session()
    print(20*'=',"Modify Student",20*'=')
    print("♦ 1. Delete Student by Name\n♦ 2. Delete Student by ID\n♦ Other Return")
    choice=input("Please Select: ")

    if choice == '1':
        name=input("Please Enter Student Name to Delete: ")
        delete_student_by_name(name,session)
    elif choice == '2':
        id=input("Please Enter Student ID to Delete: ")
        delete_student_by_id(id,session)
    else:
        session.close()
        return
    session.close()