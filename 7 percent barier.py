inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
parties = list()
votes = list()
i = 1
prt = lines[1]
vts = ''
while prt != 'VOTES:\n':
    parties.append(prt)
    votes.append(0)
    i += 1
    prt = lines[i]
i += 1
while i < len(lines):
    vts = lines[i]
    for j in range(len(parties)):
        if parties[j] == vts:
            votes[j] += 1
    i += 1
for i in range(len(parties)):
    parties[i] = (-votes[i], parties[i])
parties.sort(key=lambda x: (x[0], x[1]))
for i in range(len(votes)):
    print(parties[i][1], end='')
