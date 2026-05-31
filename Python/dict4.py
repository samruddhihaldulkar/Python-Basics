data = {}   # primary dictionary 
ndict= {}   # dictionary nested in primsry
tup = ()    # empty tuple for operations in dictionary
lis = []    # emplty list for operations in dictionary


# adding values in an empty list
num_in = int(input("Enter the number of elemnts you want to add in the list: "))
for i in range(num_in):
    numele= input("Enter the element in the list: ")
    lis.append(numele)
print(lis)    
# adding values in an empty tuple
num = int(input("Enter the no of elemnts in tuple: "))
print()
for i in range(num):
    etup = input(f"Enter the {i+1} element: ")
    tup+=(etup,) 
print(tup)    


# adding key-value pair in a dictionary
num_in = int(input("Enter the number of elemnts you want to add in the dictionary: "))
for i in range(1,num_in+1):
    roll_num= input("Enter the roll_num  of stu: ")
    name = input("Enter the  name of stu: ")

print(data)


 
# adding key value pairs in the ndict according to the primary dictionary key
num_in = int(input("Enter the number of elemnts you want to add in the dictionary: "))
for i in range(1,num_in+1):
    roll_num= input("Enter the roll_num  of stu: ")
    name = input("Enter the  name of stu: ")
    ndict={}
    num_in1 = int(input("Enter the number of games you want to add : "))
    for i in range(1,num_in1+1):
        game= input("Enter the  name of the game: ")
        gnum = int(input("Enter the  gersy num : "))
        
    # adding ndict in dict
    data[roll_num]={
        "name":name,
        "game-name":game,
        "g-no":gnum
}
print(data)

#using tuple as a key in a dictionary
ntup=(1,2,3,4,5,6)
predict={}
predict[ntup]="tuple as a key"
print(predict)