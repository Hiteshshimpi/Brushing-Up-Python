s = "abca"
i = 0
j = len(s) - 1
val = True
count = 0


def checkPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


while i < j:
    left = s[i]
    right = s[j]
    if left != right:
        result = checkPalindrome(s, i + 1, j)
        result1 = checkPalindrome(s, i, j - 1)
        if result or result1:
            val = True
        else:
            val = False
    i += 1
    j -= 1

print(val)
