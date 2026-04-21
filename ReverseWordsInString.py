s = "the sky is blue"
str1 = ""


def reverseWords(s, str1) -> str:
    words = s.split()
    n = len(words) - 1
    print(words)
    while n >= 0:
        str1 += words[n] + " "
        n = n - 1
    return str1.rstrip()


result = reverseWords(s, str1)
print(result)
