def get_min_value(nums):
    prefix = [nums[0]]
    neg_ = nums[0]
    for i in range(1,len(nums)):
        prefix.append(nums[i]+prefix[-1])
        if(prefix[i]<neg_):
            
            neg_ = prefix[i]

    if (neg_<1):
        return abs(neg_) + 2
    return neg_

out = get_min_value([-3,2,-3,4,2])
print(out)