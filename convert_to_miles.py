# объявление функции
def convert_to_miles(km):
    miles = km * 0.6214
    return round(miles, 5)
# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))