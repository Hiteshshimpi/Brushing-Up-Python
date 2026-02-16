myDict={"st1":49,"st2":32}
print(myDict['st1'])
print(myDict.get('st2'))

#add element
myDict["st3"]=47
myDict["st4"]=77
myDict["st5"]=23
print(myDict)

#iterate over dictonary

#for key in myDict:
    #print(key, myDict[key])


# aslo ddoing this .keys

for key in myDict.keys():
    print(key,myDict[key])

print("Values  ***********")
# for printing only values

for val in myDict.values():
    print(val)

print("Both  ***********")
# if we want both
for key, val in myDict.items():
    print(key,val)


# check if key is present
# Traditional for loop

for key in myDict.keys():
    if key == "st1":
        print("Presnt")

# another way i.e optimzed way

if "st1" in myDict.keys():
    print("Present in Dictionary")

