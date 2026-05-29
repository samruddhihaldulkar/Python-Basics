'''tup = ()
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
print("final tuple is: ",tuple(lst))'''

# Do it wiothout converting it into a list