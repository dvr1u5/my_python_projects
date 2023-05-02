x, y = int(input()), int(input())
if x == 1:
    x1 = True
else:
    x1 = False
if y == 1:
    y1 = True
else:
    y1 = False


def xor(x, y):
    return (x or y) and not (x and y)
if xor(x1, y1):
    print(1)
else:
    print(0)
