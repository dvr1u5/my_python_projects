K = int(input())
count = 0
D = 1
while D <= K:
    N = D
    simp = N
    M = 0
    while N != 0:
        M = M * 10 + N % 10
        N = N // 10
    if M == simp:
        count += 1
    D += 1
print(count)
