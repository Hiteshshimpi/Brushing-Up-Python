grid =[[1,2,3],[4,5,6],[7,8,9]]
print(grid)

print(grid[0][1])

# input the 2D matrix using list comprehension


n =int(input()) # row
m=int(input()) # column
grid1=[]

for i in range(n):
    grid1.append([int(ele) for ele in input().split()])


print(grid1)