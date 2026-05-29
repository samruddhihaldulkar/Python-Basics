#Simple Calculator

while True:
    input("Press Enter to continue using the calculator")
    nxt=input("DO YOU WANT TO PERFORM ANOTHER OPERATION: (y/n): \nPress y for Yes or n for No: ")
    if nxt!="y":
        break


    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    op=input("Enter a operator: ")
    if op=="+":
        print("Sum is : ",num1+num2)
    elif op=="-":
        print("Sub is : ",num1-num2)
    elif op=="*":
        print("Mul is : ",num1*num2)
    elif op=="/":
        if num2==0:
            print("ERROR: Division by zero")
            continue
        else:
            print("Div is : ",num1/num2)
    else:
        print("Invalid Operator")
