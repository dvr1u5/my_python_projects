NumList = list(map(int, input().split()))
num = 0
for i in range(0, len(NumList) - 1):
    for j in range(i + 1, len(NumList)):
        if NumList[i] == NumList[j]:
            num += 1
print(num)
