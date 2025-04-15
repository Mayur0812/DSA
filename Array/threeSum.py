
def threeSum( nums):
    result = []
    if (len(nums)< 3):
        return []
    if (len(nums)==3):
        if sum(nums)==0:
            return nums
        else:
            return []
    
    nums.sort()
    print(f"Sorted array : {nums}")
    for num in range(0, len(nums)):
        l = num
        r = len(nums) -1
        while l < r:
            print(nums[num],nums[l],nums[r])
            curr_sum = nums[num] + nums[l] + nums[r]
            if curr_sum == 0:
                print(f"Zero for: {num, l, r}")
                result.append([num,l,r])
                l,r = l+1, r-1
            elif curr_sum > 0:
                r = r-1
            else:
                l = l + 1
    
    return result

if __name__ == '__main__':        
    print(threeSum([-1,0,1,2,-1,-4]))