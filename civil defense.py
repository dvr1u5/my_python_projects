n = int(input())
NumList = list(map(int, input().split()))
m = int(input())
NumList2 = list(map(int, input().split()))
village = list()
bombshelter = list()
numbombshelter = list()
for i in range(n):
    tempVillage = (int(NumList[i]), i + 1)
    village.append(tempVillage)
for i in range(m):
    tempBombshelter = (int(NumList2[i]), i + 1)
    bombshelter.append(tempBombshelter)
for i in village:
    mindistantion = abs(bombshelter[0][0] - i[0])
    p = bombshelter[0][1]
    for j in bombshelter:
        if mindistantion > abs(j[0] - i[0]):
            mindistantion = abs(j[0] - i[0])
            p = j[1]
    numbombshelter.append(p)
print(*numbombshelter)
