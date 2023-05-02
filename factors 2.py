def number_of_factors(num):
    numbers = 0
    for i in range(1, num+1):
        if num % i == 0:
            numbers += 1
    return numbers
# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))