N = int(input())
summ = 0
while N != 0:
    M = N
    N = int(input())
    if N > M:
        summ += 1
print(summ)
