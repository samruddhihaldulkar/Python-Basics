print("====== Attendance Management System ======")

students = []
attendance = []

while True:

    print("\n1. Add Students")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Attendance Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        n = int(input("Enter number of students: "))

        for i in range(n):
            name = input("Enter student name: ")
            students.append(name)
            attendance.append("Not Marked")

        print("\nStudents added successfully.")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo students found.")

        else:
            for i in range(len(students)):

                status = input(students[i] + " (P/A): ")

                if status == "P" or status == "p":
                    attendance[i] = "Present"

                elif status == "A" or status == "a":
                    attendance[i] = "Absent"

                else:
                    attendance[i] = "Invalid"

            print("\nAttendance marked successfully.")

    elif choice == "3":

        if len(students) == 0:
            print("\nNo student records available.")

        else:
            print("\n----- Attendance Report -----")

            for i in range(len(students)):
                print(students[i], "-", attendance[i])

    elif choice == "4":

        present = 0
        absent = 0

        for status in attendance:

            if status == "Present":
                present = present + 1

            elif status == "Absent":
                absent = absent + 1

        print("\n----- Attendance Summary -----")
        print("Total Students :", len(students))
        print("Present Students :", present)
        print("Absent Students :", absent)

    elif choice == "5":

        print("\nExiting Program...")
        break

    else:
        print("\nInvalid choice. Try again.")