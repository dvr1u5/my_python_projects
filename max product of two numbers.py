NumList = list(map(int, input().split()))
maxplus = NumList[0]
maxplus2 = NumList[1]
maxminus = 0
maxminus2 = 0
for i in range(0, len(NumList)):
    if NumList[i] > maxplus:
        maxplus2 = maxplus
        maxplus = NumList[i]
    elif NumList[i] > maxplus2:
        maxplus2 = NumList[i]
    if NumList[i] < 0 and abs(NumList[i]) > abs(maxminus):
        maxminus2 = maxminus
        maxminus = NumList[i]
    elif NumList[i] < 0 and abs(NumList[i]) > abs(maxminus2):
        maxminus2 = NumList[i]
if maxplus * maxplus2 > maxminus * maxminus2:
    print(maxplus2, maxplus)
else:
    print(maxminus, maxminus2)
