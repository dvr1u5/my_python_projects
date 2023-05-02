from functools import reduce

print(
        *map(
                lambda a: reduce(
                        lambda x, y: abs(x - y), a), zip(
                                *map(
                                        lambda x: map(int, input().split()), range(int(input())))
                )
        )
)
