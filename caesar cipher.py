print('Введите строку')
line = input()
print('Что делаем - шифрование или дешифрование?')
direction = input()
print('Какой язык алфавита - русский или английский?')
language = input()
print('Введите шаг сдвига')
step = int(input())
rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if direction == 'шифрование' and language.lower() == 'русский':
    for i in range(len(line)):
        if line[i].isalpha():
            print(rus[(rus.index(line[i]) + step) % 32 + 32 * ((rus.index(line[i])) // 32)], end='')
        else:
            print(line[i], end='')
if direction == 'шифрование' and language.lower() == 'английский':
    for i in range(len(line)):
        if line[i].isalpha():
            print(eng[(eng.index(line[i]) + step) % 26 + 26 * ((eng.index(line[i])) // 26)], end='')
        else:
            print(line[i], end='')
if direction == 'дешифрование' and language.lower() == 'русский':
    for i in range(len(line)):
        if line[i].isalpha():
            print(rus[(rus.index(line[i]) - step) % 32 + 32 * ((rus.index(line[i])) // 32)], end='')
        else:
            print(line[i], end='')
if direction == 'дешифрование' and language.lower() == 'английский':
    for i in range(len(line)):
        if line[i].isalpha():
            print(eng[(eng.index(line[i]) - step) % 26 + 26 * ((eng.index(line[i])) // 26)], end='')
        else:
            print(line[i], end='')

