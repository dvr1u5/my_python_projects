numList = list(map(int, input().split()))
num = 0
i = 1
while i < len(numList) - 1:
    if numList[i] > numList[i-1] and numList[i] > numList[i+1]:
        num += 1
    i += 1
print(num)
