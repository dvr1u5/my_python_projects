N = int(input())
length = 0
prev = 0
bigorsmall = 1
maxn = 0
while N != 0:
    prev = N
    N = int(input())
    if N == 0:
        if length < maxn:
            maxn = length
    elif (N > prev and bigorsmall == 1) or (N < prev and bigorsmall == -1):
        length += 1
    elif N < prev and bigorsmall == 1:
        bigorsmall = -1
        if length > maxn:
            maxn = length
        length = 1
    elif N > prev and bigorsmall == -1:
        bigorsmall = 1
        if length > maxn:
            maxn = length
        length = 1
    elif N == prev:
        if length > maxn:
            maxn = length
        length = 0
print(maxn + 1)
