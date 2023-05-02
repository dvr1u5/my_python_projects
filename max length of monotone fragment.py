N = int(input())
num = 0
maxnum = 0
bigorsmall = 1
maxn = 0
while N != 0:
    maxnum = N
    N = int(input())
    if N == 0:
        if num > maxn:
            maxn = num
    elif (N > maxnum and bigorsmall == 1) or (N < maxnum and bigorsmall == -1):
        num += 1
    elif N < maxnum and bigorsmall == 1:
        bigorsmall = -1
        if num > maxn:
            maxn = num
        num = 1
    elif N > maxnum and bigorsmall == -1:
        bigorsmall = 1
        if num > maxn:
            maxn = num
        num = 1
    elif N == maxnum:
        if num > maxn:
            maxn = num
        num = 0
print(maxn + 1)
