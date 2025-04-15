import numpy as np
def largest_sum(s,k):
    l=r=ans=0
    for i in range(len(s)):
        arr_sum = np.sum(s[i:i+k])
        ans = max(arr_sum,ans)
    return ans 

out = largest_sum([3,-1,4,12,-8,5,6],4)
print(out)