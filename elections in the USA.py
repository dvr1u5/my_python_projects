inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
electiondict = {}
for i in lines:
    surname, votes = i.split()
    electiondict[surname] = electiondict.get(surname, 0) + int(votes)
electiondict2 = dict(sorted(electiondict.items()))
for i in electiondict2:
    print(i, electiondict2[i])
