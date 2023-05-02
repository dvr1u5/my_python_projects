N = int(input())
summ = 0
if N % 2 == 0:
    summ += 1
while N != 0:
    N = int(input())
    if N % 2 == 0:
        summ += 1
print(summ - 1)
