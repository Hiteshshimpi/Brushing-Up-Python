d ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s="III"
n = len(s)
sums=0
i=0
while i < n :
    if  i < n-1 and d[s[i]] < d[s[i+1]] :
        val = d[s[i + 1]] - d[s[i]]
        sums += val
        i += 2
    else:
        sums+=d[s[i]]
        i+=1
print(sums)