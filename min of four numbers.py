def min4(q, w, e, r):
    return min(min(q, w), min(e, r))

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))
