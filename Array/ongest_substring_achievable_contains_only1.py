def find_length(s):
    l=ans=0
    count_0 = 0
    
    for r in range(len(s)):
        if s[r] == '0':
            count_0+=1
        while count_0>1:
            if s[l]=="0":
                count_0+=-1
            l+=1
        ans = max(ans, r-l+1)
    return ans


out = find_length("0111")
print(out)