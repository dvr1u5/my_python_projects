N = int(input())
M = 1
max2 = 0
while M != 0:
    M = int(input())
    if M > N:
        max2 = N
        N = M
    elif M <= N and M > max2:
        max2 = M
print(max2)
