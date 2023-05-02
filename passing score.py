inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
K = int(lines[0])
partip = list()
students = 0
summ = 0
summpred = 0
scorepred = 0
r = list()
l = 0
for i in range(1, len(lines)):
    r = lines[i].split()
    partip.append((int(r[-3]), int(r[-2]), int(r[-1])))


def scoresumm(score):
    return (score[0] + score[1] + score[2]) * (-1)
partip.sort(key=scoresumm)
for i in partip:
    if i[0] >= 40 and i[1] >= 40 and i[2] >= 40:
        students += 1
        l += 1
        summ = -scoresumm(i)
        if summ != summpred:
            l = 0
            scorepred = summpred
    if students > K:
        if l > K:
            summpred = 1
        elif summpred == summ:
            summpred = scorepred
        break
    summpred = summ
if students <= K:
    print(0)
elif scorepred == 0:
    print(1)
else:
    print(summpred)
