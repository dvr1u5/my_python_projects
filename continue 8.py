N = int(input())
M = 1
max = 1
while M != 0:
    M = int(input())
    if M > N:
        N = M
        max = 1
    elif M == N:
        max += 1
print(max)
