N = list(map(int, input().split()))
number = 1
i = 0
while i < (len(N) - 1):
    if N[i] != N[i + 1]:
        number += 1
    else:
        i += 1
print(number)
