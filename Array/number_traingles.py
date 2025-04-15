def count_trinagles(a):
    count = 0
    #a.sort()   # nlogn
    n = len(a)     # n
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if( (a[i]+a[j]>a[k]) and(a[i]+a[k]>a[j])and (a[j]+a[k]>a[i])):
                    count+=1
    return count


if __name__ == "__main__":
    arr = [10, 21, 22, 100, 101, 200, 300]
    # Function call
    print("Total number of triangles possible is",
          count_trinagles(arr))
