inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
NList = list()
for i in lines:
    s, name, c, p = i.split()
    partip = (s, name, int(p))
    NList.append(partip)
    NList.sort()
for i in NList:
    print(*i, file=outFile)
inFile.close()
outFile.close()
