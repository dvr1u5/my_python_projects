N = int(input())
synonimsdict = {}
for i in range(N):
    synonims = input().split()
    synonimsdict[synonims[0]] = synonims[1]
    synonimsdict[synonims[1]] = synonims[0]
word = input()
print(synonimsdict[word])
