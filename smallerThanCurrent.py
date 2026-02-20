def smallerNumbersThanCurrent(nums):
    myList = []
    unsortedNums = nums.copy()
    nums.sort()
    for i in range(len(nums)-1):
        ind =unsortedNums.index(nums[i])
        myList.insert(ind,i)

    return myList


lit=smallerNumbersThanCurrent([8,1,2,2,3])
print(lit)