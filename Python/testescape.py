'''
write a python program to input 3 strings from a user i.e., name, age and address. using a single print function, print the strings in 3 lines the the following format:
name=<name>
age=<age>
address=<address>
'''

str1=input("Enter Name : ")
str2=int(input("Enter Age : "))
str3=input("Enter Address : ")

print("Name=",str1,"\n","Age=",str2,"\n","Address=",str3)

'''
some escape sequences used in python:
1. \n -> new line
2. \t -> horizontal tab
3. \" -> for printing double quotation
4. \' -> for printing single quotation
5. \r -> move the cursor to the beginning of the current line
6. \\ -> used for printing backslash
7. \0 -> represents the end of string
8. \f -> advance to the next page
9. \v -> vertical tab
10. \b -> move the cursor one position backwards
'''