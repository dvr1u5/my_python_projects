inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
dict1 = {}
for i in lines:
    name, good, number = i.split()
    dict2 = []
    f = 0
    if name in dict1:
        dict2 = dict1[name]
    for j in range(len(dict2)):
        if dict2[j][0] == good:
            f = 1
            t = (dict2[j][0], dict2[j][1] + int(number))
            dict2[j] = t
    if f == 0:
        dict2.append((good, int(number)))
    dict1[name] = dict2
dict1 = dict(sorted(dict1.items()))
for i in dict1:
    print(i, ':', sep='')
    t = dict1[i]
    t.sort()
    for j in t:
        print(*j)
