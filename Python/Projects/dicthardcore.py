student={}
bol=True
while bol:
    
    name_key1=input("Enter a dictionary key: ")
    value1=input("Enter a value to the key: ")
    student[name_key1]=value1
    data={}
    nums=int(input("Enter the number of student you want to add: "))
    for i in range(1,nums+1):
        stu=input("Enter the name of student: ")
        data[stu]={
            "name":stu,    
        }
    subject={}
    numsub=int(input("Enter the number of subject "))



    choice= input("Do you want to add more items(y/n): ")
    if choice.lower()=="y":
        continue
    elif choice.lower()=="n":
        bol = False
    else:
        print("Invalid choice")
        break
print(data)    