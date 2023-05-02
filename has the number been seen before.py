NumList = list(map(int, input().split()))
NumList2 = set()
for i in NumList:
    if i in NumList2:
        print('YES')
    else:
        print('NO')
    NumList2.add(i)
