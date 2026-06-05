#Question 2
'''
Two friends have their own friend lists stored as sets.
Create a program that:
Finds mutual friends
Finds unique friends of each person
Suggests friends based on set difference
Counts total unique friends
Allows adding and removing friends'''

flist1 = {"ram","sham","neha","riya","priya"} #firend 1 list

flist2 = {"neha","riya","priya","dev","sid"} # friend 2 list

#Finds mutual friends
mfriend = flist1.intersection(flist2)
print("Mutual friends are: ",mfriend)

#Finds unique friends of each person 
ufriend1 = flist1.difference(flist2)
ufriend2 = flist2.difference(flist1)

print("Unique friends of friend 1:",ufriend1)
print("Unique friends of friend 2:",ufriend2)

#Suggests friends based on set difference
print("Suggested friends for friend 1: ",ufriend2)
print("Suggested friends for friend 2: ",ufriend1)

#Counts total unique friends
count1 = 0
for friend in ufriend1:
        count1 +=1
print("unique friend of Friend 1 = ",count1) 

count2 = 0
for friend in ufriend1:
        count2 +=1
print("unique friend of Friend 2 = ",count2) 

print("Total unique friend: ",count1+count2)

#Allows adding and removing friends
flist1.add("sam")
flist2.remove("sid")

print(flist1)
print(flist2)






