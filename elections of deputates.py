inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
electiondict = {}
numofvotes = {}
dapohuy = []
summ = 0
firstnum = 0
for i in lines:
    votes = [int(votes) for votes in i.split() if votes.isdigit()]
    name = i[:-len(str(votes[-1])) - 2]
    electiondict[name] = votes[-1]
    summ += votes[-1]
places = 0
firstnum = summ / 450
for j in electiondict:
    res = electiondict[j] // firstnum
    res2 = (electiondict[j] / firstnum) % 1
    places += res
    numofvotes[j] = int(res)
    dapohuy.append((-res2, -electiondict[j], j))
if places < 450:
    remainder = 450 - places
    dapohuy.sort()
    k = 0
    while remainder > 0:
        numofvotes[dapohuy[k][2]] += 1
        remainder -= 1
        k += 1
for i in numofvotes:
    print(i, numofvotes[i])
