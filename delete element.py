numList = list(map(int, input().split()))
k = int(input())
numList = numList[0:k] + numList[k+1::]
print(*numList)
