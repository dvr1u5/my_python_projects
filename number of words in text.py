inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
wordcount = set()
for j in lines:
    words = j.split()
    for i in words:
        wordcount.add(i)
print(len(wordcount))
