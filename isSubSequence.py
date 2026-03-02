def isSubSequence(s, t):
    count=0
    indexVals=0
    for i in range(len(s)):
        indexvalofT = t.find(s[i])
        if s[i] in t and indexvalofT >= indexVals:
            count+=1
            indexVals=indexvalofT

    print(count)
    if count==len(s):
        return True
    else:
        return False

def isSubSequence2(s, t):
    sp=0
    for i in range(len(t)):
        if t[i] == s[sp]:
            if sp ==len(s)-1:
                return True
            sp+=1

    return False




#print(isSubSequence("abc","ahbgdc"))
#print(isSubSequence("abc","ahbgdc"))
print(isSubSequence2("abc","ahbgdc"))