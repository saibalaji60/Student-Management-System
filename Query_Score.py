'''
    Author : Naga Suresh Kalla
    Date : 11-30-2023
'''

from Utilities import isNotNone
from Database import Session
from CURD import get_score_by_name, get_score_by_id, update_score_by_id

session = Session()


def query_score():
    while True:

        print("♦ 1. Display Student Score by Name\n♦ 2. Update Student Score by ID\n♦ Other Return")
        choice = input("Please Select: ")
        if choice == '1':
            name = input("Please Enter Student Name to Display the Score: ")
            scores = get_score_by_name(name, session)
            if isNotNone(scores):
                print_scores(scores)
            else:
                print(" ✖ No record Found")
        elif choice == '2':
            try:
                idd = input("Please Enter Student ID to Update the Score: ")
                check = get_score_by_id(idd, session)

                if isNotNone(check):
                    while True:
                        a = input("New grade for CS 1030 (press enter without modification): ")
                        if a.isdigit():
                            break
                        else:
                            print(" ✖ Invalid grade ")
                    while True:
                        b = input("New grade for CS 1100 (press enter without modification): ")
                        if b.isdigit():
                            break
                        else:
                            print(" ✖ Invalid grade ")

                    while True:
                        c = input("New grade for CS 2030 (press enter without modification): ")
                        if c.isdigit():
                            break
                        else:
                            print(" ✖ Invalid grade ")

                    update_score_by_id(idd, a, b, c, session)
                    print("  ✔ Record Updated successfully")
                else:
                    print(" ✖ No record Found")
            except :
                session.close()
                break
        else:
            session.close()
            break


def print_scores(scores):
    print("=====================================Student Record=====================================")
    print(f"{'  ID':10} | {' Name':20} | {'CS1030':8} | {'CS1100':8}| {'CS20230':8}|")
    for student in scores:
        print(
            f"{student.id:10} | {student.name:20} | {student.CS1030:8} | {student.CS1100:7} | {student.CS2030:7} |")
    print(40 * '=')
