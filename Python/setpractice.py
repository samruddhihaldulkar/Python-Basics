# Python Set Operations Menu-Driven Program
'''
Question:

Write a menu-driven Python program to perform various operations on two sets entered by the user.

The program should display the following menu repeatedly until the user chooses to exit:

1. Union
2. Intersection
3. Difference (A - B)
4. Difference (B - A)
5. Symmetric Difference
6. Add Element to Set A
7. Remove Element from Set A
8. Check Membership
9. Display Sets
10. Exit

*Requirements:*

Accept two sets from the user at the beginning of the program.
Perform the selected operation based on the user's choice.
Use appropriate set methods and operators.
Display the result of each operation.
Continue showing the menu until the user selects Exit.
'''
fruits = {"apple","banana","mango","grapes","tomato"}  #set A
veggie = {"potato","onion","peas","tomato"}   #set B

while True:
    print("------Menu------")
    print("1.Union  \n 2.Intersection  \n 3. Difference (A - B)\n 4.Difference (B - A) \n 5. Symmetric Difference \n 6.Add Element to Set A \n 7.Remove Element from Set A \n 8.Check Membership \n 9. Display Sets \n 10.Exit")
    choice = int(input("Enter the choice: "))

    match choice:
        case 1 :
            union_set = fruits.union(veggie)
            print(union_set)

        case 2:
            intersect_set = fruits.intersection(veggie)  
            print(intersect_set)  

        case 3 :
            difference1 = fruits.difference(veggie)
            print(difference1)

        case 4 :
            difference2 = veggie.difference(fruits)
            print(difference2)

        case 5 :
            sdiff = fruits.symmetric_difference(veggie)        
            print(sdiff)

        case 6 : 
            fruits.add("cherry")
            print(fruits)    

        case 7 :
            fruits.remove("apple")
            print(fruits)    

        case 8 :
            x = input("Enter the element: ")
            if x in fruits:
                print("Element found in fruits!!")

            elif x in veggie:
                print("Element found in veggie!!")

            else:
                print("Element not found!")

        case 9 :
            print(fruits)
            print(veggie)

        case 10 : 
            break

