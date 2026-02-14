# woc to print the factorical of a number

# using loop style
# print("Enter a Number: ")
# num = int(input())
# sums= 1
# while( num >=1):
#     sums*=num
#     num-=1
#
# print(sums)



# now recursive way
def myFunc1(n):
    if n<=1:
        return
    count = n*n-1
    n= n-1
    myFunc1(n)

myFunc1(3)
