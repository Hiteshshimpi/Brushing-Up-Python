def closestNumberToZero(nums):
    closest = nums[0]
    for i in nums:
        if abs(i) < abs(closest):
            closest = i
        if i < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

nums = [2,-1,1]
print(closestNumberToZero(nums))