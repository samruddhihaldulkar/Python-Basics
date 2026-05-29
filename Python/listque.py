#Write a program to take user input and create 2 list  of natural numbers aand extend the first list using the extent function.
a=[]
b=[]
num_in1 = int(input("enter  number of elements in first list"))
for i in  range(num_in1):
    numele = int(input("Enter the element"))
    a.append(numele)
num_in2 = int(input("enter number of elemnts in 2 list")) 
for i in range(num_in2):
    numele2 = int(input("Enter the element"))
    b.append(numele2)  
print(a)
print(b)

a.extend(b)
print(a)


