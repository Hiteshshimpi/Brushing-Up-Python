# myStr =" Hitesh Shimpi"
# # or
# myStr1= 'Hitesh SHimpi'
#
# # for complete sentence
# mysenTence =''' Hitesh shimpi is good guy and lovable person'''
# print(myStr)
# print(myStr1)
# print(mysenTence)
#
# #input string
#
# str = input()
# print(str)
#
# str= 'banana'
# # inbuild method
# # count, split , strip
# print(str.count('a',0,4))  # it takes string and tell how many time that string has occured in the givemn str
#


#ascii value

x ='a'
print(x,ord(x))
print(x,chr(ord(x)+3))

ans=""
str ="hiteShISAGood"
for char in str:
    if ord(char) >=90:
        ans += char
    else:
        ans += chr(ord(char)+ ord('a') - ord('A'))

print(ans)