n = int(input())
FM2 = 0
FM1 = 1
simp = 2
while simp <= n:
    simp += 1
    F = FM1 + FM2
    FM2 = FM1
    FM1 = F
if n == 1:
    print(FM1)
elif n == 0:
    print(FM2)
else:
    print(F)
