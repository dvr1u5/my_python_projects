from math import sqrt

print(2, *filter(
        lambda a: 0 not in set(
            map(
                lambda x: a % x, range(2, int(sqrt(a))+1))),
            range(3, int(input())+1, 2)
    )
)
