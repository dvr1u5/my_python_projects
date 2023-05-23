import random

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
confusable = 'il1Lo0O'
chars = ''
print('Введите количество генерируемых паролей')
num_of_passwords = int(input())
print('Введите длину пароля')
length_of_password = int(input())
print('Включать ли цифры 0123456789?')
answ = input()
if answ.lower() == 'да':
    chars += digits
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
answ2 = input()
if answ2.lower() == 'да':
    chars += uppercase_letters
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
answ3 = input()
if answ3.lower() == 'да':
    chars += lowercase_letters
print('Включать ли символы', punctuation + '?')
answ4 = input()
if answ4 == 'да':
    chars += punctuation
print('Исключать ли неоднозначные символы', confusable + '?')
answ5 = input()
if answ5 == 'да':
    for i in confusable:
        chars = chars.replace(i, '')
if answ.lower() != 'да' and answ2.lower() != 'да' and answ3.lower() != 'да' and answ4.lower() != 'да':
    print('Вы долбаеб, введите хоть где-то "да"!1!!!!!')
for i in range(num_of_passwords):
    print(generate_password(length_of_password, chars))




