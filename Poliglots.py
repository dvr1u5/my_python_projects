N = int(input())
lng = set()
lng2 = set()
for i in range(N):
    M = int(input())
    languages = set()
    for j in range(M):
        languages.add(input())
    if i == 0:
        lng = languages
    lng &= languages
    lng2 |= languages
print(len(lng))
print(*lng, sep='\n')
print(len(lng2))
print(*lng2, sep='\n')
