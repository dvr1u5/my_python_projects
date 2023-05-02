N, K = input().split()
N = int(N)
K = int(K)
NumList = list()
for i in range(N):
    NumList.append('I')
for i in range(K):
    l, r = input().split()
    l = int(l)
    r = int(r)
    for j in range(l - 1, r):
        NumList[j] = '.'
print(*NumList, sep='')
