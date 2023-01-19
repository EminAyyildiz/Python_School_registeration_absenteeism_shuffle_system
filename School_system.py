# Written by Emin Ayyıldız
print("Written by Emin Ayyıldız")

import random
import time

def create_student():
    name = input("Enter student's name : ")
    number = input("Enter student's number : ")
    class_ = input("Enter student's class : ")
    branch = input("Enter student's branch : ")
    absenteeism = input("Number of days the student is absent from school : ")
    with open("students.txt", "a") as file:
        file.write(f"Name: {name}, Number: {number}, Class: {class_}, Branch: {branch}, Absenteeism: {absenteeism}\n")
    print("Student is registered. Please wait....")
    time.sleep(1.5)
    print("Student created!")

def view_student():
    number = input("Enter student's number: ")
    with open("students.txt", "r") as file:
        for line in file:
            if number and f"Number: {number}" in line:
                print("The student you are looking for is displayed... Please wait...\n")
                time.sleep(1.5)
                print(line)
                break
        else:
            print("Student not found.")

def change_class_between_class():
    branch1 = input("Enter first branch: ")
    branch2 = input("Enter second branch: ")
    students_branch1 = []
    students_branch2 = []
    with open("students.txt", "r") as file:
        for line in file:
            if branch1 in line:
                students_branch1.append(line)
            elif branch2 in line:
                students_branch2.append(line)
    if students_branch1 and students_branch2:
        with open("studentsnewlist.txt", "w") as file:
            for student in students_branch1:
                if random.random() > 0.5:
                    file.write(student.replace(branch1, branch2))
                else:
                    file.write(student)
            for student in students_branch2:
                if random.random() > 0.5:
                    file.write(student.replace(branch2, branch1))
                else:
                    file.write(student)
        print("The branches you specified are shuffled, Please wait...")
        time.sleep(2)
        print("Branches shuffled!")
    else:
        print("One or both of the branches have no students.")

def check_absenteeism():
    class_ = input("Enter student's class : ")
    with open("students.txt", "r") as file:
        print(f"Those who failed in the {class_} are listed. Please wait")
        time.sleep(2)
        print(f"Students who fail the class due to their absence from {class_} branch: \n")
        for line in file:
            if class_ in line:
                for absenteeism in line.split(','):
                    if "Absenteeism" in absenteeism:
                        if int(absenteeism.split(':')[1]) >= 10:
                            print(line)
                            break

def check_admin_credentials(username, password):
    if username == "admin" and password == "1234":
        print("Logging into account, please wait...")
        time.sleep(1.5)
        print("Login to the system.")
        return True

    elif username == "q" or username == "Q" or password == "Q" or password == "q":
        print("The system has been logged out.")
        quit()
    else:
        print("Wrong username or password...")
        return False

while True:
    print("Welcome to school system. We wish you a nice day..\n")
    username = input("Please enter username :")
    password = input("Please enter password : ")
    if check_admin_credentials(username, password):
        while True:
            print("\nSchool System Menu \n")
            print("1. Create student")
            print("2. View student")
            print("3. Shuffle class")
            print("4. Atttendance Control")
            print("5- EXIT")
            choice = input("Enter choice: ")
            if choice == "1":
                create_student()
            elif choice == "2":
                view_student()
            elif choice == "3":
                change_class_between_class()
            elif choice == "4":
                check_absenteeism()

            elif choice == "5":
                print("EXITING....")
                time.sleep(1.5)
                print("BYE BYE")
                break
            else:
                print("Invalid choice")

