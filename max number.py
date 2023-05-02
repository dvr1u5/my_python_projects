N = int(input())
num = 0
maxnum = 0
while N != 0:
    simp = N
    N = int(input())
    if N == simp:
        num += 1
    elif maxnum < num:
        maxnum = num
        num = 0
    else:
        num = 0
print(maxnum + 1)
