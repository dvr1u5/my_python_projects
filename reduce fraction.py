n = int(input())
m = int(input())


def ReduceFraction(n, m):
    d = gsd(n, m)
    return n // d, m // d


def gsd(a, b):
    if b == 0:
        return a
    return gsd(b, a % b)
print(*ReduceFraction(n, m))
