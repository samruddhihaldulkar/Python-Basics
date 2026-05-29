#write a program to check whether string is palindrome or not 
while True:
    name=input("Enter a name ")
    if name[::-1]==name:
        print("Name is palindrome")
        
    else:
        print("name is not a palindrome")