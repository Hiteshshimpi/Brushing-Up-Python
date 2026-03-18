n = 5
results = []
for i in range(1, n - 1):
    results.append(list[:])
    results[i].append(list[1])
    prevList = results[i - 1]
    for j in range(1, i - 1):
        results[i].append(prevList[j - 1] + prevList[j])
    results[i - 1].append([1])

print(results)
