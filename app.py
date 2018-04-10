student_list = []

def create_student():
    # Ask the user for the student's name
    name = input("Enter Student's Name: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data

def add_mark(student, mark):
    # Append a mark to the student dict
    student['marks'].append(mark)


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number 

def print_student_details(student):
    print("{}, average mark: {}.".format(student['name'],
                                        calculate_average_mark(student)))

def print_student_list(student):
    for i, student in enumerate(student):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    # Add a student to student list
    selection = input("Enter 'p' to print the student list,"
                       "'s' to add a new student,"
                       "'a' to add a mark to a student,"
                       "or 'q' to quit. ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
            
        selection = input("Enter 'p' to print the student list,"
                       "'s' to add a new student,"
                       "'a' to add a mark to a student,"
                       "or 'q' to quit. ")

menu()