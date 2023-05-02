kilometres = list(map(int, input().split()))
tariff = list(map(int, input().split()))
summ = 0
kilometres.sort()
tariff.sort(reverse=True)
for i in range(len(kilometres)):
    coust = kilometres[i] * tariff[i]
    summ += coust
print(summ)
