total = 0
for x in range(1, 65):
    for y in range(1, 60):
        for z in range(1, 45):
            if 28 * x + 30 * y + 31 * z == 365:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
