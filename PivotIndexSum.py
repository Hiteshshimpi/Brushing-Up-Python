def pivotSumeIndex(nums):
    leftsum =0
    rightSum=0
    for i in range(len(nums)):
        rightSum=rightSum+nums[i]
    print(rightSum)

    for i in range(len(nums)-1):
        if leftsum == rightSum - nums[i]:
            print(i)
            break
        else:
            leftsum= leftsum+nums[i]
            rightSum= rightSum- nums[i]


nums= [1,7,3,6,5,6]
pivotSumeIndex(nums)

# leftsum=0
# for i in range(len(nums)):
#     rightsum=0
#     for j in range(i+1,len(nums)):
#         rightsum=rightsum+nums[j]
#
#     if leftsum==rightsum:
#         print(i)
#         break
#     else:
#         leftsum= leftsum+nums[i]
#
# print(leftsum)



