a = int(input())
b = int(input())


def gsd(a, b):
    if b == 0:
        return a
    return gsd(b, a % b)
print(gsd(a, b))
