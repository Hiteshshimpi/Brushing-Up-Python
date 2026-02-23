# dnf alogo , here we sort 0s,1s,2s without using any sorting algorithm
# i.e we have 3 pointer 1 low, 2 ,mid, 3 high


def dnfAlgo(nums):
    low = 0
    high = len(nums)-1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid+=1
        elif nums[mid] == 1:
            mid+=1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

    return nums

nums=[2,0,1]
print(dnfAlgo(nums))