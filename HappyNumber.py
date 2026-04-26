def isHappy(n: int) -> bool:
    def sumOfDigits(n) -> int:
        sum = 0
        while n > 0:
            dig = n % 10
            sum = sum + (dig * dig)
            n = n // 10
        return sum

    slow = n
    fast = n
    while fast != 1:
        slow = sumOfDigits(slow)
        fast = sumOfDigits(sumOfDigits(fast))

        if fast == 1:
            return True

        if slow == fast:
            return False

    return True


n = 2
print(f" result is : {isHappy(n)}")
