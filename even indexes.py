a = list(input().split())
num = 0
for i in range(len(a)):
    if int(a[i]) > 0:
        num += 1
print(num)
