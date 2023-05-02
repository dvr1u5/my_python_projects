inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
wordsdict = {}
for i in lines:
    words = i.split()
    for j in words:
        wordsdict[j] = wordsdict.get(j, 0) + 1
wordslist = list()
for i in wordsdict:
    wordslist.append((-wordsdict[i], i))
wordslist.sort()
for i in wordslist:
    print(i[1])
