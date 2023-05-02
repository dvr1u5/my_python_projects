NumList = set(map(int, input().split()))
NumList2 = set(i for i in range(min(NumList), max(NumList) + 1))
print(len(NumList & NumList2))
