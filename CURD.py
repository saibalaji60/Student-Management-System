'''
    Author : Naga Suresh Kalla
    Date : 11-30-2023
'''

from Database import User, Student, Score


def add_user(username, password, session):
    new_user = User(name=username, password=password)
    session.add(new_user)
    session.commit()


def get_all_users(session):
    usernames = session.query(User.name).all()
    return [username[0] for username in usernames]


def get_password_of_user(username, session):
    user = session.query(User).filter(User.name == username).first()
    if user:
        return user.password


def get_all_student(session):
    usernames = session.query(Student).all()
    return usernames


def get_all_student_by_name(user, session):
    usernames = session.query(Student).filter(Student.name == user).all()
    return usernames


def get_all_student_by_id(user, session):
    usernames = session.query(Student).filter(Student.id == user).all()
    return usernames


def add_student_data(name, age, gender, major, phone, session):
    student = Student(name=name, age=age, major=major, phone=phone, gender=gender)
    session.add(student)
    session.commit()
    print(student.id)
    score = Score(id=student.id, name=name, CS1030=0, CS1100=0, CS2030=0)
    session.add(score)
    session.commit()


def get_score_by_name(username, session):
    usernames = session.query(Score).filter(Score.name == username).all()
    return usernames


def get_score_by_id(idd, session):
    usernames = session.query(Score).filter(Score.id == idd).all()
    return usernames


def update_score_by_id(idd, a, b, c, session):
    score = session.query(Score).filter(Score.id == idd).first()
    if score:
        score.CS1030 = a
        score.CS1100 = b
        score.CS2030 = c
        session.commit()


def update_student_id(student, age, major, phone, session):
    student.age = age
    student.major = major
    student.phone = phone
    session.commit()


def delete_student_by_id(idd, session):
    student = session.query(Student).filter(Student.id == idd).first()
    if student:
        session.delete(student)
        session.commit()
        delete_score_of_student(student.id,session)
        print(f" ✔ Record deleted Successfully")
    else:
        print(f" ✖ No Record Found")


def delete_student_by_name(uname, session):
    student = session.query(Student).filter(Student.name == uname).first()
    if student:
        session.delete(student)
        session.commit()
        delete_score_of_student(student.id, session)
        print(f" ✔ Record deleted Successfully")
    else:
        print(f" ✖ No Record Found")
def delete_score_of_student(idd,session):
    score = session.query(Score).filter(Score.id == idd).first()
    if score:
        session.delete(score)
        session.commit()