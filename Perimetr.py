import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)


x1, y1, x2, y2, x3, y3 = int(input()), int(input()), \
                         int(input()), int(input()), \
                         int(input()), int(input())
print(distance(x1, y1, x2, y2) +
      distance(x3, y3, x2, y2) + distance(x1, y1, x3, y3))
