n = 3

m = n
steps = 0
while n > 0:
    n = n - 1
    if n >= 0:
        steps = steps + 1
while m > 0:
    m = m - 2
    if m > 0:
        steps = steps + 1

print(steps)
####

n = 5
op = []
ones = []
twos = []

# ones
sum = 0
for i in range(1, n):
    sum = sum + 1
    ones.append(1)
    if sum == n:
        op.append(ones)
        print(op, ones)
        break
    # elif sum < n:

sum2 = 0
for i in range(1, n):
    sum2 = sum2 + 2
    twos.append(2)
    if sum == n:
        op.append(twos)
        print(op, twos)
        break
    elif n - sum == 1:
        twos.append(2)

print(len(op))
