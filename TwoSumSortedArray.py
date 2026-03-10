numbers=[2,7,11,15]
target=9
def twoSumSortedArray(numbers, target):
    start=0
    end =len(numbers)-1
    res=[]

    while start<end:
        if numbers[start]+numbers[end]==target:
            res.append(numbers[start])
            res.append(numbers[end])
            break
        elif numbers[start]+numbers[end]>target:
            end-=1
        else:
            start+=1
    return res


print(twoSumSortedArray(numbers,target))