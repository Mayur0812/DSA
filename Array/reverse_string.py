def reverse(arr_):
    i = 0
    j = len(arr_)-1

    while (i <j):
        arr_[i],arr_[j] = arr_[j],arr_[i]
        i +=1
        j -=1
    return arr_

print(reverse(["H","a","n","n","a","h"]))