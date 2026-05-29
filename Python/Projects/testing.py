'''Create a program to:
Mark student attendance
Count present/absent students
Display attendance summary
Write a Python program that maintains the attendance of students in a class. The program should repeatedly display a menu and allow the user to perform different attendance-related operations.
The system should allow the user to:
1. Add student names
2. Mark attendance as Present or Absent
3. View attendance report
4. Count present and absent students
5. Exit the program'''
names= []
status=[]
pcount=0
acount=0
while True :      
    print("------Menu------")
    print("1.Add student names  \n 2.Mark attendance as Present or Absent \n 3.View attendance report  \n 4.Count present and absent students\n 5.Exit")
    choice = int(input("Enter the choice: "))
    match choice:
        case 1:
            name=input("Enter the name of student: ")
            names.append(name)
            print(names)
        case 2 :
            attend = input("Enter present or absent: ")
            status.append(attend)
            print(status)
        case 3 :
            zipped = list(zip(names,status))
            print(zipped)
        case 4 :
            for char in status:
                if char=="present":
                    pcount+=1
                else:
                    acount+=1
            print("Number of present student ",pcount)
            print("Number of absent student ",acount)         
        case 5 :
            print("Exit")
            break
        
