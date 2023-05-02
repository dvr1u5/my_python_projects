a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(33):
    for j in range(33):
        for k in range(33):
            if a != b and a != c and a != d and b != c and b != d and c != d:
                print(a ** 3 + b ** 3, c ** 3 + d ** 3)
