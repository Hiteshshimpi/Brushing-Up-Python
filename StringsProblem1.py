# check if string is palindrome or not. i.e if the reverse of that string is the same as the original string


str = "ABCDFCBA"
isPalindrome = True
length = len(str)

for i in range(len(str)/2):
    if str[i] != str[length-1 -i]:
        isPalindrome = False
        break
print(isPalindrome) 