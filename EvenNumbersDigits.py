nums = [12,345,2,6,7896]
count=0
for i in range(len(nums)):
    val = str(nums[i])
    if len(val) % 2 == 0:
        count=count+1
print(count)
