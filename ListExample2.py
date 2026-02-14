import sys
myList=[]
n =int(input("Enter a number: "))
minVal=100
maxVal=0
for i in range(n):
    currElement = int(input("Enter a number: "))
    myList.append(currElement)
    if currElement <= minVal and currElement >= maxVal:
        minVal=currElement
        maxVal=currElement
    elif currElement <= minVal:
        minVal=currElement

print(f"Max values is {max(myList)}")
print(f"MIn values is {min(myList)}")
print("Min val is",minVal)
print("Max values is",maxVal)