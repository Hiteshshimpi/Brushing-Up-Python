nums = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
i = 0
j = 1
result = 1
n = len(nums)
while (j < n):
    if nums[i] == nums[j]:
        j += 1
        continue
    else:
        nums[i + 1] = nums[j]
        i += 1
        j += 1
        result += 1

print(result)
