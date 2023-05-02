import math
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print('3')
elif a == 0 and b == 0 and c != 0:
    print('0')
elif a == 0 and b != 0:
    x1 = -c / b
    print('1', "{:.6f}".format(x1))
elif d == 0:
    x1 = -b / (2 * a)
    print('1', "{:.6f}".format(x1))
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 < x2:
        print('2', "{:.6f}".format(x1), "{:.6f}".format(x2))
    else:
        print('2', "{:.6f}".format(x2), "{:.6f}".format(x1))
elif d < 0:
    print('0')
