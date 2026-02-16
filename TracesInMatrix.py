n = int(input())
m= int(input())

grid=[]
for i in range(n):
    grid.append([int(ele) for ele in input().split()])
print(grid)


trace =[]
count =0
for i in range(n):
    for j in range(m):
        if i==j:
            count+= grid[i][j]
            trace.append(grid[i][j])

print(count)
print(trace)
