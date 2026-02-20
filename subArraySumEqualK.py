def subarraySum(nums, k):
    sum = 0
    count = 0
    for i in range(len(nums)):
        if len(nums) < 2 and k==0:
            return 0
        if nums[i] >=0:
            sum = sum + nums[i]
            if sum >= k :
                count = count + 1
            elif k==0:
                count=1
            else:
                sum = 0

    return count

nums=[-1,-1,1]
k=2
print(subarraySum(nums, k))