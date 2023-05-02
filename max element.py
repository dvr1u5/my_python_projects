numList = list(map(int, input().split()))
ind = 0
max = numList[0]
for i in range(1, len(numList)):
    if numList[i] > max:
        max = numList[i]
        ind = i
print(max, ind)
