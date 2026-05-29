str1=input("Enter a String: ")

#length of string 
print(len(str1))

#lower case 
#converts any uppercase character from the string into lower case
print(str1.lower())

#upper case
#converts any lower case character into upper case
print(str1.upper())

#capitalize
#makes the first letter capital
print(str1.capitalize())

#title
#capitalizes the first letter of eveery word
print(str1.title())

#strip
#remove spaces from both sides
#s = " sam "
#s.strip() generates output as sam AND removes spaces from the start and end of the string 
print(str1.strip())
print(str1.lstrip())    #removes spaces from the left
print(str1.rstrip())    #removes spaces from the right


