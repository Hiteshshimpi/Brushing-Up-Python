#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string ""

#Input: strs = ["flower","flow","flight"]
#Output: "fl"

strs = ["flower","flow","flight"]
prefixStr=""
a,b,c=0,0,0

for i in range(len(strs)):
    val = strs[a][i]
    print(val,end=" ")
    a+=1


