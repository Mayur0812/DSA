def subArray(s,k):
    l=r=0
    curr = 1
    ans = 0
    for r in range(0,len(s)):
        curr*=s[r]
        while(curr>=k):
            curr//=s[l]
            l+=1
        ans +=  r-l+1
    return ans
        
out = subArray([10, 5, 2, 6],100)
print(out)