s = "Mr Ding"
words = s.split()
firstRes = ""
sart = 0

while sart < len(words):
    n = len(words[sart]) - 1
    firstRes += words[sart][n]
    n -= 1
    sart += 1
print(firstRes)
