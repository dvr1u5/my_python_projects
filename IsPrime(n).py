import math
def is_prime(num):
    i = num + 1
    while True:
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                break
            j += 1
        else:
            return i
        i = i + 1

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))