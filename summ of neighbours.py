n = int(input())
lines = []
for i in range(n):
    line = input()
    lines.append(line)
k = int(input())
for i in range(len(lines)):
    if i == k:
        print(lines[i])
