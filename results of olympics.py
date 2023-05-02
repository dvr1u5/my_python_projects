inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
classes = list()
points = list()
winners9 = 0
winners10 = 0
winners11 = 0
max9 = -1
max10 = -1
max11 = -1
for i in lines:
    s, name, c, p = i.split()
    classes.append(int(c))
    points.append(int(p))
for i in range(len(points)):
    if classes[i] == 9:
        if points[i] > max9:
            max9 = points[i]
            winners9 = 1
        elif points[i] == max9:
            winners9 += 1
    elif classes[i] == 10:
        if points[i] > max10:
            max10 = points[i]
            winners10 = 1
        elif points[i] == max10:
            winners10 += 1
    elif classes[i] == 11:
        if points[i] > max11:
            max11 = points[i]
            winners11 = 1
        elif points[i] == max11:
            winners11 += 1
print(winners9, winners10, winners11)
