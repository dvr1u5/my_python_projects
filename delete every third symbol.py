s = input()
i = 0
while i != len(s):
    if i % 3 != 0:
        print(s[i], sep='', end='')
    i = i + 1
