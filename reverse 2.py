numList = list(map(int, input().split()))
for i in range(0, len(numList) // 2):
    j = numList[i]
    numList[i] = numList[len(numList) - 1 - i]
    numList[len(numList) - 1 - i] = j
print(*numList)
