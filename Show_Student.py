'''
    Author : Naga Suresh Kalla
    Date : 11-30-2023
'''

from welcome import display_welcome_page_file, replace_text_in_file
from CURD import get_all_student,get_all_student_by_name,get_all_student_by_id
from Database import Session


def student_views(username):
    if username:
        session = Session()
        while True:
            display_welcome_page_file("showstudent.txt")

            choice = input("Please select (1 - 3): ")

            if choice == '1':
                try:
                    students = get_all_student(session=session)
                    if len(students) == 0:
                        print("✖ No Student existing")
                        break
                    else:
                        print_students(students)
                except:
                    print("Error in Show All Students")
            elif choice == '2':
                try:
                    student_name=input("Please Enter Student Name to Display: ")
                    students = get_all_student_by_name(student_name,session=session)
                    if len(students) == 0:
                        print("✖ No Student existing")
                        break
                    else:
                        print_students(students)
                except:
                    print("Error in Show All Students by Name")
            elif choice == '3':
                try:
                    student_id=input("Please Enter Student ID to Display: ")
                    students = get_all_student_by_id(student_id,session=session)
                    if len(students) == 0:
                        print("✖ No Student existing")
                        break
                    else:
                        print_students(students)
                except:
                    print("Error in Show All Students by ID")
            else:
                session.close()
                break


def print_students(students):
    print("=====================================Student Record=====================================")
    print(f"{'  ID':10} | {' Name':20} | {'Age':3} | {'Gender':5}| {' Major':15} |   ☎")
    for student in students:
        print(
            f"{student.id:10} | {student.name:20} | {student.age:3} | {student.gender:5} | {student.major:15} | {student.phone}")
    print(75*'=')



