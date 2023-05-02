inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
classes = list()
points = list()
max9 = 0
max10 = 0
max11 = 0
for i in lines:
    s, name, c, p = i.split()
    classes.append(int(c))
    points.append(int(p))
for i in range(len(points)):
    if classes[i] == 9:
        if points[i] > max9:
            max9 = points[i]
    elif classes[i] == 10:
        if points[i] > max10:
            max10 = points[i]
    elif classes[i] == 11:
        if points[i] > max11:
            max11 = points[i]
for i in range(len(points)):
    if points[i] == max9 and classes[i] == 9:
        points[i] = 0
    if points[i] == max10 and classes[i] == 10:
        points[i] = 0
    if points[i] == max11 and classes[i] == 11:
        points[i] = 0
max9 = 0
max10 = 0
max11 = 0
for i in range(len(points)):
    if classes[i] == 9:
        if points[i] > max9:
            max9 = points[i]
    elif classes[i] == 10:
        if points[i] > max10:
            max10 = points[i]
    elif classes[i] == 11:
        if points[i] > max11:
            max11 = points[i]
print(max9, max10, max11)
