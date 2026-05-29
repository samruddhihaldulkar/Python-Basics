'''wap to add key 3 key value  pairs in a dictionarty also the third key should be fruits and the value
associated to it must be a list of the fruits that should be created by a user'''
final = {}
fruits=[]
par_in= 3
for i in range(3):
    key= input("Enter the key : ")
    
    if i==2:
        value_in=int(input("Enter the number of fruits you want in list: "))
        for j in range(value_in):
            fruitsin= input("Enter the name of fruit: ")
            fruits.append(fruitsin)
        final[key]=fruits  
    else:
        value=input("Enter the value: ")
        final[key]=value
print(final)                      
