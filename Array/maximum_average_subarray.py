import numpy as np
def max_avg_sub(s,k):
    avg = 0
    sum= 0 
    ans = -999999
    for i in range(k):
        sum+= s[i]

    avg = sum/k
    ans = avg
    
    for i in range(k,len(s)):
        sum = sum + s[i] - s[i-k]

        avg = float(sum/k)
        ans = max(ans,avg)
    return ans

out = max_avg_sub([1,12,-5,-6,50,3],4)
print(out)

