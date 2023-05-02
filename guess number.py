n = int(input())
line = input()
set1 = set()
set2 = set()
set3 = set(str(i) for i in range(1, n+1))
while line != 'HELP':
    answer = input()
    lines = line.split()
    set4 = set() #все ее ответы
    for i in lines:
        set4.add(i)
    if answer == 'YES':
        if len(set1) == 0:
            set1 = set4
        set1 &= set4
    if answer == 'NO':
        set2 |= set4
    line = input()
if len(set1) == 0:
    print(*sorted(set3 - set2))
else:
    print(*sorted(set1 - set2))
