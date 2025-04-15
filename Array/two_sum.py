def twosum(arr_, target):
    i = 0
    j = len(arr_) - 1


    while i < j:
        if arr_[i] + arr_[j] == target:
            print("Returning True")
            return True
        if arr_[j] + arr_[i] < target:
            i+=1
        if arr_[j] + arr_[i] > target:
            j-=1

    return False

twosum([1, 2, 4, 6, 8, 9, 14, 15],target=28)
print(twosum)