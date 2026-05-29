#Write a programme To slice a list To exclude first third and last elements
a=['samruddhi_gadhi',77,4,3,6,9,'gadhi_samruddhi']
for i in range(len(a)):
    if i ==0:
        continue
    elif i ==3:
        continue
    elif i ==len(a)-1:
        continue
    else:
        print(a[i])