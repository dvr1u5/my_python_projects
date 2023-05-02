import math
n = float(input())
c = n - math.floor(n)
if c < 0.5:
    print(int(n))
else:
    print(math.ceil(n))
