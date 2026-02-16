grid =[[1,2,3],[4,5,6],[7,8,9]]
n=len(grid)
m= len(grid[0])
print(n)
print(m)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if j > i:
            temp = grid[j][i]
            grid[j][i]= grid[i][j]
            grid[i][j] = temp

for i in range(n):
    print(grid[i])