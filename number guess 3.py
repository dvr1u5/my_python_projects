import random
print('Добро пожаловать в числовую угадайку')
print('Введите ответ')
num = input()

def is_valid(number):
    if number.isdigit() == True:
        if 1 <= int(number) <= 100:
            return True
        else:
            return False
    while is_valid(number) != True:
        if is_valid(number) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            number = input()
        else:
            number = int(number)

rndmnum = random.randint(1, 100)

while num != rndmnum:
    num = input()
    if int(num) < rndmnum:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        num = input()
    elif int(num) > rndmnum:
        print('Ваше число больше загаданного, попробуйте еще разок')
        num = input()
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
