N = int(input())
simp = N
summ = 1
while N != 0:
    N = int(input())
    simp += N
    summ += 1
print(simp / (summ - 1))
