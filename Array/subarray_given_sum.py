def sub_sum(a,sum):
    """
    Assuming all non-negative integers
    """
    n = len(a)
    for i in range(n):
        sum_till_now = a[i]
        for j in range(i+1,n):
            sum_till_now+=a[j]
            if(sum_till_now==sum):
                print(f"Subarray exists between indices {i} to {j}")
                return
            if(sum_till_now>sum):
                break

def optimised(a,sum):
    """
    1. Idea is to keep track of start ptr
    2. keep adding elements till sum is greater than desired.
    3. move element from start index to next one and check with next element by adding it
    4. if sum is equal, return
    else repeat 1-4
    """
    n = len(a)
    start_ptr = 0
    subarr = a[start_ptr]
    i = 1
    while i <n:
        #print(f"Subarray right now is: {subarr}")
        if(subarr<sum):
            subarr+=a[i]
            i = i+1
        if(subarr==sum):
            print(f"subarray found between indices {start_ptr} and {i-1}")
            return
        if(subarr>sum):
            #print(f"Current sum is: {subarr} Removing {start_ptr} with value: {a[start_ptr]}")
            subarr-=a[start_ptr]
            start_ptr+=1
    print("Not found")


if __name__ == "__main__":
    #arr = [15,2,4,8,9,5,10,23]
    arr = [1, 4, 20, 3, 10, 5]
    n = len(arr)
    sum = 23
    sub_sum(arr, sum)
    optimised(arr,sum)


