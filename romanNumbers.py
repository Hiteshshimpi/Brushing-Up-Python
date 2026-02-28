dictRomanVals ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
print(dictRomanVals.get('I'))

romanVal="IV"
sums=0
for i in romanVal:
    val = dictRomanVals.get(i)
    print(val)
    sums = sums + val

print(sums)