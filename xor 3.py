NumList = list(map(int, input().split()))
for i in zip(NumList):
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 1
    elif a == 1 and b == 0:
        return 1
    elif a == 1 and b == 1:
        return 0
