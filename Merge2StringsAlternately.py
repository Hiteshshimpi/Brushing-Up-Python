word1 ="abcd"
word2 ="pq"

strResult =""
#check which  string is greater in length
i=0
j=0
word1Length = len(word1)
word2Length = len(word2)

while i<word2Length and j<word1Length:
    strResult += word1[i]
    strResult += word2[j]
    i=i+1
    j=j+1
z = len(strResult)
if word1Length>word2Length:
    strIndex = z - word2Length
    strResult += word1[strIndex:]
    #for i in range(strIndex,word1Length):
        #strResult += word1[i]
else:
    strIndex = z - word1Length
    for i in range(strIndex,word2Length):
        strResult += word2[i]

print(strResult)
