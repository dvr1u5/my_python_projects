N, K = input().split()
N = int(N)
K = int(K)
wknd = set(range(7, N + 1, 7)) | set(range(6, N + 1, 7))
strikes = set()
for i in range(K):
    item = tuple(map(int, input().split()))
    days = set(range(item[0], N + 1, item[1]))
    strikes |= days
print(len(strikes - wknd))
