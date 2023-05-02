x = list()
y = list()
a = 0
for i in range(0, 8):
    m, n = input().split()
    x.append(int(m))
    y.append(int(n))
for i in range(0, 7):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] \
                or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            a = 1
if a == 1:
    print('YES')
else:
    print('NO')
