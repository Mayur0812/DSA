def sign_diff(a,b):
    if((a>0) and (b<0)):
        return True
    elif((a<0) and (b>0)):
        return True
    else:
        return False
def rearr(a):
    n = len(a)
    i = 0
    ptr = 0
    while i < n-1:
        print(f"checking: {a[i]} and {a[i+1]} : Sign diff is: {sign_diff(a[i],a[i+1])}")
        if (sign_diff(a[i],a[i+1])):
            i+=1
            ptr = i
            continue
        print(f"i is: {i} and array is: {a}")
        while (sign_diff(a[i],a[i+1])!=True):
            i+=1
        a[ptr+1],a[i+1] = a[i+1],a[ptr+1]
        ptr = ptr+1
        if(ptr<n-2):
            i = ptr
        print(f"array is : {a}")
    return a

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
arr = [1,2,3,-4]
arr = [1,2,3,4,-5,-6,-7,-8,9,10]
print(rearr(arr))



            
            