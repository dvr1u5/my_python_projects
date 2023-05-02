numList = list(map(int, input().split()))
for j in range(0, len(numList)):
    if numList[j] % 2 != 0:
        min = numList[j]
        break
for i in range(1, len(numList)):
    if numList[i] % 2 != 0:
        if numList[i] < min:
            min = numList[i]
print(min)
