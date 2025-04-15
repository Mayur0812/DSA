def isSub(arr1, arr2):
    i=j=0

    while (i< len(arr1) and j < len(arr2)):
        if arr1[i] == arr2[j]:
            i +=1
            j+=1
        else:
            j +=1
        if i==len(arr1):
            print("returning True")
            return True
    print("Nope")
    return False

isSub('acz','abcde')
