def summ():
    n = int(input())
    if n == 0:
        return n
    else:
        return n + summ()
print(summ())
