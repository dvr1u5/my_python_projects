for x in range(1, 100):
    for y in range(1, 200):
        for z in range(1, 300):
            if 10 * x + 5 * y + 0.5 * z == 100 and x + y + z == 100:
                print(x, y, z)