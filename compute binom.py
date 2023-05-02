# объявление функции
def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial
def compute_binom(n, k):
    binom = factorial(n) // (factorial(k) * factorial(n-k))
    return binom
# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
