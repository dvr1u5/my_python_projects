# объявление функции
def get_month(language, number):
    ru = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'augest', 'september', 'october', 'november', 'december']
    if lan == 'ru':
        return ru[num - 1]
    if lan == 'en':
        return en[num - 1]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
