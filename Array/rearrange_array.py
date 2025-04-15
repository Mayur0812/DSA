def rearrange(a):
    n = len(a)
    res = [0] * n
    for i in range(n):
        res[i] = i if i in a else -1
    return res

arr = [1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrange(arr))
