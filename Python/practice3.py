#detect vowels in a given string and replace them with *
a= input("Enter a string: ")
result=""
for char in a:
    if char == "a" or char=="i" or char=="o" or char =="e" or char=="u":
        result += "*"
    else:
        result += char
print(result)            

