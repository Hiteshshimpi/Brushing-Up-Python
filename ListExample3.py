#mean median and mode of the list

#mean
myList =[1,2,3,4,5,6,7,8,9]
sums=0
for i in myList:
    sums = sums + i
print(sums/len(myList))



#median
myList1=[]
print("Enter the lenth of the list")
n=int(input("Enter a number: "))

for i in range(n):
    currElement =int(input("Enter a number: "))
    myList1.append(currElement)

if n % 2 != 0:
    medianOfOdd = (0 + n-1) / 2
    print(myList1[int(medianOfOdd)])
else:
    medianOfEven = (0 + n) / 2
    medAvg = myList1[int(medianOfEven)] + myList1[int(medianOfEven-1)]
    print(medAvg / 2)