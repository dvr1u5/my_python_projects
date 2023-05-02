val = int(input())
sqrt_val = int(val ** 1/2)


def lagrange(val, n_terms):
    if n_terms != 0:
        sqrt_val = int(val ** 1/2)
    else:
        return False
    if sqrt_val ** 2 != val:
        if sqrt_val > 0:
            if not lagrange(val - sqrt_val ** 2, n_terms - 1):
                sqrt_val -= 1
            else:
                return str(sqrt_val) + ' ' + lagrange(val - sqrt_val**2, n_terms - 1)
        else:
            return
    else:
        return str(sqrt_val)
print(lagrange(val, 4))
