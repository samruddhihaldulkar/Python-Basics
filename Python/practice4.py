#input a list from the user and sort it's elements into ascending order 
a=[]
num_in=int(input("Enter the number of elements in the list: "))
for i in range(num_in):
    numele= int(input("Enter the element in the list: "))
    a.append(numele)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]   
for n in a:
    print(n)