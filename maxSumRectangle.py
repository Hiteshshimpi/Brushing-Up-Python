myList=[[1,2-1,-4,-20],
        [-8,-3,4,2,1],
        [3,8,10,1,3],
        [-4,-1,1,7,-6]
        ]

rows=len(myList)
cols=len(myList[0])
print(rows,cols)
currSum=0
maxSum=-2147483648
for i in range(cols):
    for j in range(rows):
        currSum=currSum +myList[j][i]
        print(f"Current Sum is :{currSum}")

    if currSum > maxSum:
        maxSum=currSum

    if currSum < 0:
        currSum=0

print(maxSum)