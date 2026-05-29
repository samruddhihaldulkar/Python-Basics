#demosntrating format and creating of dictionary
#format
'''
data={
    rn:{
        "name":n,
        "marks":{
            s1:m1,
            s2:m2,
            sn:mn
        }
    }
}
'''
# creation
data = {}

num_students = int(input("Enter number of students: "))

for d in range(1, num_students + 1):    #iteration for adding item in dictionary data
    rn=int(input(f"\nEnter rollno for student {d}:"))
    
    name = input("Enter student name: ")
    
    num_subjects = int(input("Enter number of subjects: "))
    
    marks = {}

    for i in range(1, num_subjects + 1):    #iteration for adding item in the sub-dictionary marks
        subject = input(f"Enter subject {i} name: ")
        mark = int(input(f"Enter marks for {subject}: "))
        
        marks[subject] = mark

    data[rn] = {
        "name": name,
        "marks": marks
    }

print("\nFinal Dictionary:")
print(data)

