# объявление функции
import math
def get_circle(radius):
    length = 2 * math.pi * radius
    square = math.pi * radius ** 2
    return length, square
# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)