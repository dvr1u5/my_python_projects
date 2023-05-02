NumList = list(map(int, input().split()))
cntNum = [0] * (max(NumList) + 1)


def CountSort(NumList):
    for i in NumList:
        cntNum[i] += 1
    for j in range(len(cntNum)):
        print((str(j) + ' ') * cntNum[j], end='')
CountSort(NumList)
