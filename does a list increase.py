numList = list(map(int, input().split()))


def IsAscending(numList):
    i = 1
    while i < len(numList) and numList[i] > numList[i-1]:
        i += 1
    if i >= len(numList):
        print('YES')
    else:
        print('NO')


IsAscending(numList)
