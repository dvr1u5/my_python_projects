a = int(input())
b = int(input())


def summ(a, b):
    if b == 0:
        return a
    else:
        return summ(a, b - 1) + 1
print(summ(a, b))
