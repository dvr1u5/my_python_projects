inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
wordsdict = {}
for i in lines:
    wordlist = list(map(str, i.split()))
    for j in wordlist:
        wordsdict[j] = wordsdict.get(j, 0) + 1
        print(wordsdict[j] - 1, end=' ')
