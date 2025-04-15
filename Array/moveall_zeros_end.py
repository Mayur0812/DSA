def push_zero(a):
    n = len(a)
    for i in range(0,n):
        if(a[i]==0):
            a.pop(i)
            a.insert(len(a)+1,0)
    return a
a = [1,2,0,4,3,0,5,0]
a = push_zero(a)
print(a)

