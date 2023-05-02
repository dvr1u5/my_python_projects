import math
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 < x2:
        print("{:.6f}".format(x1), "{:.6f}".format(x2))
    else:
        print("{:.6f}".format(x2), "{:.6f}".format(x1))
if d < 0:
    print('')
if d == 0:
    x1 = -b / (2 * a)
    print("{:.6f}".format(x1))
