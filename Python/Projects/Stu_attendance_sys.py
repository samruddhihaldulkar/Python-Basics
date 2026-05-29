'''
Write a Python program that maintains the attendance of students in a class. The program should repeatedly display a menu and allow the user to perform different attendance-related operations.
The system should allow the user to:
1. Add student names
2. Mark attendance as Present or Absent
3. View attendance report
4. Count present and absent students
5. Exit the program
'''
names= []
namein="50"
pcount  = 0
acount = 0
while True :      
    print("------Menu------")
    print("1.Add student names  \n 2.Mark attendance as Present or Absent  \n 3.Count present and absent students\n 4.Exit")
    choice = int(input("Enter the choice: "))
    match choice:
        case 1:
            for i in namein:
               nameele = input("Enter the names of student : ")
               namein = nameele.split()
               names.append(namein)
               print(names)
               break      
        case 2 :
            nameele = input("Enter the names of student : ")
            namein = nameele.split()
            names.append(namein)
            print(names)
        case 3 :
            if names[[i][2]]=="present":
                pcount +=1
            else:
                acount+=1
            print("Number of present student: ",pcount)
            print("Number of absent student: ",acount)     
            
