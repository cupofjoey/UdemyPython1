def create_student():
    # Ask the user for the student's name
    name = input("Enter Student's Name: ")
    student_data = {
        'name': name,
        'marks': []
    }

s = create_student()

def add_mark(student, mark):
    # Append a mark to the student dict
    student['marks'].append(mark)

add_mark(s, 5) # Passing by reference


print(s)