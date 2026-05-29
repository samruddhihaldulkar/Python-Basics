studentrecord = {}

numele=int(input("Enter the number of student you want to add: "))

for i in range(numele):

    key= input("Enter the name of the key : ")
    value=input("Enter the roll no of student of student: ")
    keyn=input("enter the name of keyn: ")
    valuen=input("enter the name of student: ")

    subject= {}

    numsub=int(input("Enter the number of subject: "))

    for k in range(numsub):

            keys=input("enter the name of subject: ")
            valuem= int(input("enter the marks of student: "))

    subject[keys] = valuem

studentrecord[keyn] = valuen   
studentrecord[key]=  {
    studentrecord[keyn] : valuen ,
    subject[keys] : valuem
}  


print(studentrecord)

    
       

