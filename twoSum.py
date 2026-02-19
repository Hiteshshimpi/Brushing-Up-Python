def twoSum(givenNums, target):
    givenNums.sort()
    start=0
    end=len(givenNums)-1
    while start<end:
        if givenNums[start]+givenNums[end]==target:
            return [givenNums[start],givenNums[end]]
        elif givenNums[start]+givenNums[end]<target:
            start+=1
        else:
            end-=1

    return -1


givenNums=[1,5,2,10,7]
target=7
print(twoSum(givenNums,target))