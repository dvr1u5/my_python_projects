n = int(input())
plus = 1
summ = 0
while plus <= n:
    summ = summ + 1 / plus ** 2
    plus = plus + 1
epsilon = 10 ** -7
if abs(summ - int(summ)) < epsilon:
    print(int(summ))
else:
    print("{:.5f}".format(summ))
