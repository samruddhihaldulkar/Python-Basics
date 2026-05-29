#using loop fetch all the elements present at the even index check whether x=5 is the part of the list
a=[0,1,2,3,4,5,6,7,8,9,10]
for i in a:
    if a[i]==5:
        print("The element exists in the list at index: ", i)