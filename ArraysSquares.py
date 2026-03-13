# square the list of nums and then sort it
nums=[-4,-1,0,3,10]
for i in range(len(nums)):
    nums[i]= nums[i]*nums[i]
nums.sort()
print(nums)
