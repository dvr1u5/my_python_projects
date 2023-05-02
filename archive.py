S, N = input().split()
S = int(S)
N = int(N)
NumList = list()
for i in range(N):
    n = int(input())
    NumList.append(n)
summ = 0
i = 0
NumList.sort()
while i < len(NumList) and summ <= S:
    summ += NumList[i]
    i += 1
if i == len(NumList) and summ <= S:
    print(i)
else:
    print(i - 1)
