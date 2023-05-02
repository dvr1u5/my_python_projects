# объявление функции
def is_magic(date):
    numlist = date.split('.')
    for i in range(len(numlist)):
        numlist[i] = int(numlist[i])
    if numlist[0] * numlist[1] == numlist[2] % 100:
        return True
    else:
        return False
# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
