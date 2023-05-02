n = int(input())


def hanoi(n, i, k):
    if n == 1:
        print(1, i, k)
    else:
        tmp = 6 - i - k
        hanoi(n - 1, i, tmp)
        print(n, i, k)
        hanoi(n - 1, tmp, k)
hanoi(n, 1, 3)
