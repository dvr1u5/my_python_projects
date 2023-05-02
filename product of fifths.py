from functools import reduce

items = map(int, input().split())
product = reduce(lambda x, y: x * (y ** 5), items, 1)

print(product)
