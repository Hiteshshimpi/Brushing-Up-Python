def threeSum(givenNums, target):
    givenNums.sort()
    for i in range(len(givenNums)):
        start = i+1
        end = len(givenNums)-1
        while start < end:
            if givenNums[i] + givenNums[start] + givenNums[end] == target:
                return [givenNums[i],givenNums[start],givenNums[end]]
            elif givenNums[i] + givenNums[start] + givenNums[end] < target:
                start += 1
            else:
                end -= 1

    return -1
givenNums=[2,1,10,5,7]
target=18
print(threeSum(givenNums,target))