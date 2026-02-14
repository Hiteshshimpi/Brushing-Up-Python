n = int(input())

for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print("")



# another way to do this is using jump statements i.e break and continue

print("Enter the number of rows ")
a =int(input())
for curRow in range(a): # this will run from 0->a-1
    for curNum in range(a): # this will run from 0->a-1
        if curNum<=curRow:
            print(curNum+1, end=" ")
        else:
            #print(" ", end=" ") # instead of spaces we can add break statement to break the loop
            break
    print("")
