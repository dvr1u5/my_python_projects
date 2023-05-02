N = int(input())
NumList = list(map(int, input().split()))
NumList.sort()
sizes = list()
i = 0
while i < len(NumList) and NumList[i] < N:
    i += 1
if i < len(NumList):
    sizes.append(NumList[i])
while i < len(NumList):
    if NumList[i] - sizes[-1] >= 3:
        sizes.append(NumList[i])
    i += 1
print(len(sizes))
