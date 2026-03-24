s = "abc"
i = 0
j = len(s) - 1
val = True
count = 0
while i <= j:
    left = s[i]
    right = s[j]
    if not left.isalnum():
        i += 1
        continue
    if not right.isalnum():
        j -= 1
        continue
    if left.lower() != right.lower():
        count += 1
        if count > 1:
            val = False
            break
    i += 1
    j -= 1

print(val)
