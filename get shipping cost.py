# объявление функции
def get_shipping_cost(quantity):
    cost = 0
    for i in range(n):
        cost = 1000 + (120 * i)
    return cost
# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))