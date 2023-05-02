import math
def is_prime(num):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False

        i = i + 1
    return True
# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))