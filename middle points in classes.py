inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
classes = list()
points = list()
summ = 0
summ2 = 0
summ3 = 0
pup = 0
pup2 = 0
pup3 = 0
for i in lines:
    s, name, c, p = i.split()
    classes.append(int(c))
    points.append(int(p))
for i in range(len(points)):
    if classes[i] == 9:
        pup += 1
        summ += points[i]
    if classes[i] == 10:
        pup2 += 1
        summ2 += points[i]
    if classes[i] == 11:
        pup3 += 1
        summ3 += points[i]
mid = summ / pup
mid2 = summ2 / pup2
mid3 = summ3 / pup3
print(mid, mid2, mid3)
