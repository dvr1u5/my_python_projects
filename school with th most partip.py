inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
school = list()
num = 0
for i in lines:
    s, name, sch, p = i.split()
    school.append(int(sch))
NumSchool = list()
for i in range(max(school) + 1):
    NumSchool.append(0)
for i in school:
    NumSchool[i] += 1
maxS = max(NumSchool)
for i in range(len(NumSchool)):
    if NumSchool[i] == maxS:
        print(i, end=' ')
