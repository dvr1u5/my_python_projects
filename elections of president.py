inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
out_file = open('output.txt', 'w', encoding='utf-8')
electiondict = {}
summ = 0
for i in lines:
    electiondict[i] = electiondict.get(i, 0) + 1
electionlist = list()
for i in electiondict:
    electionlist.append((-electiondict[i], i))
    summ += electiondict[i]
electionlist.sort()
if -electionlist[0][0] > 0.5 * summ:
    out_file.write(electionlist[0][1])
else:
    out_file.write(electionlist[0][1])
    out_file.write(electionlist[1][1])
inFile.close()
out_file.close()
