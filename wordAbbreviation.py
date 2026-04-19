word = "apple"
abbr = "a3e"

i = 0
j = 0
n = len(word)
m = len(abbr)
val = True
while i < n and j < m:
    word_c = word[i]
    abbr_c = abbr[j]
    if abbr_c.isdigit():
        if abbr_c == '0':
            val = False
            break
        num = 0
        b = 0
