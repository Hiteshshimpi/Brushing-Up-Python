def maximumWealth(givenNums):
    wealth=0
    for i in range(len(givenNums)):
        sum = 0
        for j in  range(len(givenNums[0])):
            sum =sum + givenNums[i][j]
        if sum>wealth:
            wealth=sum

    return wealth

givenNums = [[1,2,3],[3,2,1]]
print(maximumWealth(givenNums))