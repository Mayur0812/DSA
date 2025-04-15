def square(x):
    return x*x
def squarers_sorted_array(s):
    res = []
    i = 0
    j = len(s) -1

    while i <= j:
        if abs(s[i]) < abs(s[j]):
            res.append(s[j] * s[j])
            j -=1
        else:
            res.append(s[i] * s[i])
            i +=1
    return res[::-1]


out = squarers_sorted_array([-7,-3,2,3,11])
print(out)