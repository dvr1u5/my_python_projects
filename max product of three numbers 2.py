NumList = list(map(int, input().split()))
NumList2 = NumList.copy()
if len(NumList) > 3:
    maxplus = max(NumList)
    NumList.remove(maxplus)
    maxplus2 = max(NumList)
    NumList.remove(maxplus2)
    maxplus3 = max(NumList)
    maxminus = min(NumList2)
    NumList2.remove(maxminus)
    maxminus2 = min(NumList2)
    NumList2.remove(maxminus2)
    maxminus3 = min(NumList2)
    if maxplus * maxplus2 * maxplus3 >= maxminus * maxminus2 * maxplus:
        print(maxplus3, maxplus2, maxplus)
    else:
        print(maxminus, maxminus2, maxplus)
else:
    print(*NumList)
