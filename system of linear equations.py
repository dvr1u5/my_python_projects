a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
B = a * d - b * c
D = e * d - b * f
S = a * f - e * c
X = D / B
Y = S / B
print("{:.6f}".format(X), "{:.6f}".format(Y))
