a = float(input())
b = float(input())
c = float(input())
pp = 1/2 * (a + b + c)
S = (pp * (pp - a) * (pp - b) * (pp - c)) ** (1/2)
epsilon = 10 ** -7
if abs(S - int(S)) < epsilon:
    print(int(S))
else:
    print("{:.6f}".format(S))
