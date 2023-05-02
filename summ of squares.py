negatives, zeros, positives = [], [], []
lst = [int(input()) for _ in range(int(input()))]

for num in lst:
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    elif num > 0:
        positives.append(num)

print(*(negatives + zeros + positives), sep='\n')