# объявление функции
def get_factors(num):
    factorslist = []
    for i in range(1, num+1):
        if num % i == 0:
            factorslist.append(i)
    return(factorslist)

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))