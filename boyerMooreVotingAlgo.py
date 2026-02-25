from itertools import count


def boyerMooreAlgo(nums):
    nums.sort()
    majorityElement = nums[0]
    count=1
    maxFeq=0
    for i in range(len(nums)-1):
        if nums[i] !=nums[i+1]:
            if maxFeq<count:
                majorityElement=nums[i]
                maxFeq=count
            count=1
        else:
            count+=1

    if maxFeq <count:
        majorityElement=nums[-1]

    return majorityElement


def boyerMooreAlgoFinal(nums):
    majorityElement=-1
    count=0
    for i in nums:
        if count ==0:
            majorityElement=i
            count=1
        else:
            if majorityElement == i:
                count+=1
            else:
                count=count-1
    return majorityElement

nums=[1,3,2,3,1]
print(boyerMooreAlgoFinal(nums))