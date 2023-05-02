# объявление функции
def get_days(month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        days = 28
    else:
        days = 31
    return days
# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))