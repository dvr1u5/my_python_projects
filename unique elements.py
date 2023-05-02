NumList = list(map(int, input().split()))
for i in range(0, len(NumList)):
    if NumList.count(NumList[i]) == 1:
        print(NumList[i], end=' ')
