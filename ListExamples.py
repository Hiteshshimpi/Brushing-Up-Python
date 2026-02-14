myList =[]
sums=0
n = int(input("Enter a number: "))
for i in range(n):
    currNum= int(input("Enter a number: "))
    myList.append(currNum)
    sums+=currNum
print(myList)
print(sums)