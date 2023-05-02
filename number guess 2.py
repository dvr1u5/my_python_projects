import random

def is_valid(number):
    if number.isdigit() == True:
        if 1 <= int(number) <= n:
            return True
        else:
            return False
    else:
        return False


def rndm_game(num):
    tries = 0
    while num != rndmnum:
        if int(num) < rndmnum:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            num = int(input())
            tries += 1
        elif int(num) > rndmnum:
            print('Ваше число больше загаданного, попробуйте еще разок')
            num = int(input())
            tries += 1
    tries += 1
    print('Вы угадали, поздравляем!', 'Ваше число попыток -', tries)


print('Добро пожаловать в числовую угадайку, до какой границы я буду загадывать? Введите число')
while True:
    n = int(input())
    rndmnum = random.randint(1, n)
    print('Введите ответ')
    num = input()
    while is_valid(num) != True:
        print('А может быть все-таки введем целое число от 1 до', n)
        num = input()
    rndm_game(num)
    print('Сыграем еще раз? Да / нет')
    answ = input()
    if answ.lower() == 'да':
        print('До какой границы я буду загадывать? Введите число')
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
