# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"


def summaryRanges(nums):
    i=0
    k=1
    for i in range(len(nums)-1):
        if nums[i] + 1 != nums[i + 1] :
            print(nums[i], end=" ")
        else:
            print(f"{nums[i]}->{nums[i + 1]}", end=" ")

def summaryRanges2(nums):
    i=0
    j=i+1
    result = []
    while i < len(nums)-1:
        if nums[j] - nums[i]==1:
            j+=1
        elif nums[i]!=nums[j-1]:
            result.append(f"{nums[i]}->{nums[j-1]}")
            i=j
            j=i+1
        else:
            result.append(f"{nums[j]}")
            i=j+1
            j=i+1

    print(result)
summaryRanges2([0,1,2,4,6,7,9])