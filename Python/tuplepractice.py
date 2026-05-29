tup = (1,2,3,4)#initialised a tuple
lst=list(tup)#typecasted the tuple into a list
print(lst)

tt=tuple(lst)#typecasted the list into a tuple
print(tt)

print(tup)
lst[3]='Samru'#updated the element of the list
print(lst[3])
print(lst)#printed the updated list
print(tuple(lst))#typecasted the updated list into a tuple


print(tup)#prints the originally initialised tuple ref= line 1
tup=tuple(lst)#overwrittern the originally initialized tuple into the tup variable
print(tup)#printed the overwrittern tup variable which basically printed the updated list typecasted as a tuple
