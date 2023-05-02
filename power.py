a = float(input())
n = int(input())


def power(a, n):
    i = 1
    r = a
    while i != n:
        if n > 0:
            r = r * a
            i = i + 1
        else:
            r = r / a
            i = i - 1
    return r
print(power(a, n))
