def find(x,arr):
    n = len(arr)
    findex = -1
    for i in range(n):
        if arr[i] == x:
            findex = i
            break
    lindex = -1
    for i in range((n-1),-1,-1):
        if arr[i] == x:
            lindex = i
            break
    return [findex,lindex]
            


arr = [1,3,5,5,5,5,67,123,125]
x =5
print(find(x,arr))