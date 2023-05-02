n = int(input())
if n == 1:
    for i in range(9, 0, -2):
        print(i, end=' ')
else:
    for i in range(10 ** n - 1, 10 ** (n - 1), -2):
        print(i, end=' ')
