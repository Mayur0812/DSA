def ways_split(s):
    prefix = s[0]
    for i in range(1,len(s)):
        prefix.append(s[i]+prefix[-1])
        