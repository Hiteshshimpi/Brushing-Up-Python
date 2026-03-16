nums=[2,3,-1,8,4]
leftsum=0
rightsum=0

for i in range(len(nums)):
    rightsum=rightsum+nums[i]

for k in range(len(nums)):
    if leftsum==rightsum - nums[k]:
        print(nums[k], k)
        break
    else:
        leftsum=leftsum+nums[k]
        rightsum=rightsum-nums[k]
