def leader(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]<=a[j] ):
                #print(f"Not adding : {a[i]}")
                break
        if(j==n-1):
            print(arr[i],end= " ")

def optimised(a):
    """
    Idea is to scan from right and print whenever max changes
    """
    last_ = len(a)-1
    
    max_ = arr[last_]
    print(a[last_],end= " ")
    for i in range(last_,-1,-1):
        #print(a[i])
        if(max_<a[i]):
            print(a[i],end = " ")
            max_ = a[i]

arr=[16, 17, 4, 3, 5, 2] 
uniq = leader(arr)
print()
optimised(arr)