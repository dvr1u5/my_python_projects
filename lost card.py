N = int(input())
summall = 0
summcards = 0
for i in range(1, N):
    n = int(input())
    summcards += n
for j in range(1, N+1):
    summall += j
ans = summall - summcards
print(ans)
