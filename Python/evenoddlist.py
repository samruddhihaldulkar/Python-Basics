#wap to seperate even and odd numbers in 2 seperate list take user input for the initial list
a= []
enum=0
onum=0
even=[]
odd=[]
num_in= int(input("Enter the number of element in the list: "))
for i in range (num_in):
    numele = int(input("Enter the elements in list: "))
    a.append(numele)
print(a)    
for i in range (num_in):
    if a[i]%2==0:
        enum=a[i]
        even.append(enum)    
    else:
        onum=a[i]
        odd.append(onum)
print("List of even num: ",even)
print("List of odd num: ", odd)             

        

