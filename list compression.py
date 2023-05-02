NumList = list(map(int, input().split()))
num = NumList.count(NumList[0])
i = 0
m = NumList[0]
while i < len(NumList):
    if NumList.count(NumList[i]) > num:
        num = NumList.count(NumList[i])
        m = NumList[i]
    i += 1
print(m)
