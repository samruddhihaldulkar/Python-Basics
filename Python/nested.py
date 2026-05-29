# Demonstrating nested dictionary creation
# Format:
'''
data = {
    roll_number: {
        "name": student_name,
        "marks": {
            subject1: mark1,
            subject2: mark2,
            ...
        }
    }
}
'''

from pprint import pprint

data = {}
num_students = int(input("Enter number of students: "))

for student_index in range(1, num_students + 1):
    roll_number = input(f"\nEnter roll number for student {student_index}: ")
    student_name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = {}
    for subject_index in range(1, num_subjects + 1):
        subject_name = input(f"Enter subject {subject_index} name: ")
        mark = int(input(f"Enter marks for {subject_name}: "))
        marks[subject_name] = mark

data[roll_number] = {
    "marks": marks,
    "name": student_name,        
}

print("\nFinal nested dictionary:")
pprint(data)

