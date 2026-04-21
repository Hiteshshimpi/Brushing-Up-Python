s = ("Mr Ding")
words = s.split()
print(words)
str1 = ""
str2 = ""

for i in range(len(words)):
    n = len(words[i]) - 1
    while n >= 0:
        str1 += words[i][n]
        n = n - 1
    str1 += " "


# print(str1.rstrip())


def reverseWordsIII(s, words, str2):
    n = len(words) - 1
    while n >= 0:
        str2 += words[n] + " "
        n = n - 1


result = reverseWordsIII(s, words, str2)
print(result)
