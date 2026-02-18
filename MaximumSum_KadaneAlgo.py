nums = [-2,1,-3,4,-1,2,1,-5,4]
curr_sum=0
maxSum=-2147483648

for i in range(len(nums)):
    curr_sum+=nums[i]
    if curr_sum > maxSum:
        maxSum=curr_sum

    if curr_sum<0:
        curr_sum=0

print(maxSum)
