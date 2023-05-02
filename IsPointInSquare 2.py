x, y = float(input()), float(input())


def IsPointInSquare(x, y):
    return y <= -x + 1 and y >= x - 1 and y >= -x - 1 and y <= x + 1
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
