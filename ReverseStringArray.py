# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["H", "a", "n", "n", "a", "h", "G"]
i = 0
j = len(s) - 1
while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j = -1

print(s)
