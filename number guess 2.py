import random

print('Добро пожаловать в числовую угадайку, до какой границы я буду загадывать? Введите число')
n = int(input())
print('Введите ответ')
num = input()

def is_valid(number):
    if number.isdigit() == True:
        if 1 <= int(number) <= n:
            return True
        else:
            return False
    else:
        return False
while is_valid(num) != True:
    print('А может быть все-таки введем целое число от 1 до', n)
    num = input()
is_valid(num)

rndmnum = random.randint(1, n)

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
rndm_game(num)
print('Сыграем еще раз? Да / нет')
answ = input()
if answ == 'да':
    print('До какой границы я буду загадывать? Введите число')
    n = int(input())
    print('Введите ответ')
    num = int(input())
    rndm_game(num)
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
