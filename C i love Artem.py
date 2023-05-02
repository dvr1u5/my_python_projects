n = int(input())
k = int(input())


def C(n, k):
    if k == 1:
        return n
    elif k == 0:
        return 1
    if n == k:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)
print(C(n, k))
