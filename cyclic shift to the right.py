NumList = list(map(int, input().split()))
max = NumList[0]
min = NumList[0]
ind = 0
ind2 = 0
for i in range(len(NumList)):
    if NumList[i] > max:
        max = NumList[i]
        ind = i
    if NumList[i] < min:
        min = NumList[i]
        ind2 = i
T = NumList[ind]
NumList[ind] = NumList[ind2]
NumList[ind2] = T
print(*NumList)
