import math
P = int(input())
X = int(input())
Y = int(input())
K = int(input())
first = 1
while K >= first:
    summ = (X * 100 + Y) * P / 100 + (X * 100 + Y)
    X = int(summ // 100)
    Y = int(summ % 100)
    first = first + 1
print(X, Y)
