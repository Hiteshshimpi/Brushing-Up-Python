myTuple = ("a", "a", "c","d","e","f","g")
print(myTuple[0])
print(myTuple,type(myTuple))

for x in myTuple:
    print(x,end=" ")

print(" ")
tupe2= myTuple.count("a")
print(tupe2)

print(myTuple.index("d"))
temp=list(myTuple)
temp[0]=6
myTup =tuple(temp)