'''Create a nested dictionary storing:
course name
faculty
credits
enrolled students
Find the course with highest enrolled students. '''
#content formation
'''
data = {
    course_data:{
        course_name{
            faculty:"mr xyz",
            students:{
                stu_name:credit
            }
        }
    }
}
'''



data = {}
num_course = int(input("Enter the number of courses: "))

for d in range(1, num_course + 1):
    course = input(f"Enter the name of course {d}: ")
    faculty = input(f"Enter the name of faculty for course {d}: ")

    students = {}
    num_students = int(input("Enter the number of students enrolled: "))

    for s in range(1, num_students + 1):
        student_name = input(f"Enter the name of student {s}: ")
        student_credits = int(input(f"Enter the credits for {student_name}: "))
        students[student_name] = student_credits

    data[course] = {
        "faculty": faculty,
        "students": students
    }

final_summary = {}
if data:
    max_course = None
    max_students = -1
    for course_name, course_info in data.items():
        student_count = len(course_info["students"])
        if student_count > max_students:
            max_students = student_count
            max_course = course_name

    final_summary = {
        "course_data": data,
        "highest_enrollment": {
            "course": max_course,
            "faculty": data[max_course]["faculty"],
            "student_count": max_students,
            "students": data[max_course]["students"],
        },
    }

print("\nFinal summary:")
print(final_summary) 