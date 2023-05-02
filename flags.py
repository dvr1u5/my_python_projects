n = int(input())
print('+___ ' * n)
for i in range(n):
    print('|', int(i + 1), ' /', sep='', end=' ')
print()
print('|__\\ ' * n)
print('|    ' * n)
