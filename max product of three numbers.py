NumList = list(map(int, input().split()))
maxminus = 0
maxminus2 = 0
maxminus3 = 0
maxplus = max(NumList[0], NumList[1], NumList[2])
maxplus3 = min(NumList[0], NumList[1], NumList[2])
maxplus2 = NumList[0] + NumList[1] + NumList[2] - maxplus - maxplus3
for i in range(0, len(NumList)):
    if i > 2:
        if NumList[i] > maxplus:
            maxplus3 = maxplus2
            maxplus2 = maxplus
            maxplus = NumList[i]
        elif NumList[i] > maxplus2:
            maxplus3 = maxplus2
            maxplus2 = NumList[i]
        elif NumList[i] > maxplus3:
            maxplus3 = NumList[i]
    if NumList[i] < 0 and abs(NumList[i]) > abs(maxminus):
        maxminus3 = maxminus2
        maxminus2 = maxminus
        maxminus = NumList[i]
    elif NumList[i] < 0 and abs(NumList[i]) > abs(maxminus2):
        maxminus3 = maxminus2
        maxminus2 = NumList[i]
    elif NumList[i] < 0 and abs(NumList[i]) > abs(maxminus3):
        maxminus3 = NumList[i]
if maxplus * maxplus2 * maxplus3 >= maxminus * maxminus2 * maxplus:
    print(maxplus3, maxplus2, maxplus)
else:
    print(maxminus, maxminus2, maxplus)
