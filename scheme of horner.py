n = int(input())
x = float(input())
a = float(input())
while n != 0:
    b = float(input())
    a = a * x + b
    n = n - 1
print("{:.2f}".format(a))
