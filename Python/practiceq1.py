#wap to input a string from the user and count character occurance input the char from the user whose occurance is to be check
a=input("Enter a string: ")
b= input("Enter a character to check the occurance: ")
count= 0
for i in a :
    if i in b:
        count+=1
print(count)    
