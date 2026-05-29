'''
tup = ()
lst = list(tup)
print(lst)
#while True:
numin=int(input("Enter the number of elements in the tuple: "))
for i in range(numin):
    numele = int(input("Enter the element: "))
    lst.append(numele)
    option=input("Enter if you want to add more element to tuple or not(y/n): ")
    if option== "y":
        continue
    else:
        break
print("final tuple is: ",tuple(lst))
'''

# Do it without type casting the tuple into list

tup=(1,2,3,4)
x = int(input("enter"))
tup+=(x,)
print(tup)