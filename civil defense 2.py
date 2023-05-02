def mindist(i, j):
    dist = abs(bombshelter[j][0] - village[i][0])
    while j < len(bombshelter) - 1:
        if abs(village[i][0] - bombshelter[j+1][0]) >= dist:
            return j
        else:
            dist = abs(village[i][0] - bombshelter[j+1][0])
            j += 1
    return j


n = int(input())
NumList = list(map(int, input().split()))
m = int(input())
NumList2 = list(map(int, input().split()))
village = list()
bombshelter = list()
i = 0
for i in range(n):
    village.append((NumList[i], i))
for i in range(m):
    bombshelter.append((NumList2[i], i))
village.sort()
bombshelter.sort()
i, j = 0, 0
answers = list()
while i < n:
    j = mindist(i, j)
    answers.append((village[i][1], bombshelter[j][1]))
    i += 1
answers.sort()
for i in answers:
    print(i[1] + 1, end=' ')
