# rotate an array by 1 left shift, using naive apporach
def rotateMyList():
    myList =[1,2,3,4,5]
    temp = myList[0]
    for i in range(1,len(myList)):
        myList[i-1]=myList[i]

    myList[len(myList)-1]=temp
    print(myList)



def rotateArraybyKtimes(nums,k):
    # to rotate array what we do is we create a rotate function from range start, k-1 and k to end and then swap them

    # check if k is value so that we dont have to run that many time
    k = k % len(nums)

    # now check if k is -gtive
    if k < 0:
        k = k + len(nums)

    # call the rotate func 3 times ,
    #1st time rotating the 1st peice
    rotateArray(nums,0,k-1)
    rotateArray(nums,k,len(nums)-1)
    rotateArray(nums,0,len(nums)-1)
    print(nums)

def rotateArray(nums,start,end):
    while start < end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1




nums = [1,2,3,4,5]
k=-1
rotateArraybyKtimes(nums,k)