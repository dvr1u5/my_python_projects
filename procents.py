import math
P = int(input())
X = int(input())
Y = int(input())
summ = (X * 100 + Y) * P / 100 + (X * 100 + Y)
print(int(summ // 100), int(summ % 100))
