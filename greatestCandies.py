def kidsWithCandies(candies,extraCandies):
    myCandyList=[]
    maxCandies =max(candies)
    for i in candies:
        extraCandiesSum = 0
        extraCandiesSum= extraCandies + i
        if extraCandiesSum >= maxCandies:
            myCandyList.append(true)
        else:
            myCandyList.append("false")

    return myCandyList

candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies,extraCandies))