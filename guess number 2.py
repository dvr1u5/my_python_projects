n = int(input())
line = input()
set3 = set(int(i) for i in range(1, n+1))
while line != 'HELP':
    lines = line.split()
    set4 = set()
    for i in lines:
        set4.add(int(i))
    set4 &= set3
    if len(set4) <= len(set3) // 2:
        print('NO')
        set3 -= set4
    else:
        print('YES')
        set3 = set4
    line = input()
print(*sorted(set3))
