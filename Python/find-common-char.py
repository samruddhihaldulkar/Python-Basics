#wap to find common character between two string
s1=input("Enter a string :  ")
s2=input("Enter a string :  ")
for char in s1:
    if char in s2:
        print(char)