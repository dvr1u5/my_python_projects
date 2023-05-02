n = int(input())
keys = list(map(int, input().split()))
k = int(input())
pressing = list(map(int, input().split()))
cnttaps = [0] * (n + 1)


def kbrd(keys, pressing):
    for i in pressing:
        cnttaps[i] += 1
    for i in range(1, len(cnttaps)):
        if cnttaps[i] > keys[i-1]:
            print('YES')
        else:
            print('NO')
kbrd(keys, pressing)
