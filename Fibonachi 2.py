FM2 = 0
FM1 = 1
simp = 2
F = 1
A = int(input())
while A > F:
    simp += 1
    F = FM1 + FM2
    FM2 = FM1
    FM1 = F
if A == F:
    print(simp - 1)
elif A == 0:
    print(0)
else:
    print(-1)
