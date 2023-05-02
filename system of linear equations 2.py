a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == b == c == e == d == f == 0:
    print(5)
elif (a == b == 0 and e != 0) or (c == d == 0 and f != 0):
    print(0)
elif a * d == c * b or e * d == b * f:
    if b == d == 0:
        if a != 0 and c != 0:
            print(3, e / a)
        elif a == 0 and e == 0:
            print(3, f / c)
        elif c == 0 and f == 0:
            print(3, e / a)
    elif a == c == 0:
        if b != 0 and d != 0:
            print(4, e / b)
        elif b == 0 and e == 0:
            print(4, f / d)
        elif d == 0 and f == 0:
            print(4, e / b)
    elif b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
else:
    B = a * d - b * c
    D = e * d - b * f
    S = a * f - e * c
    X = D / B
    Y = S / B
    print(2, X, Y)
