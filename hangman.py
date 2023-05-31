import random

word_list = ['переход', 'ветер', 'замок', 'пол', 'дурак', 'процесс', 'ручка', 'академия', 'спина', 'подъезд', 'тон', 'ресурс', 'сад', 'штука', 'дверь', 'грех', 'собственность', 'хозяйство', 'представитель', 'описание', 'угроза', 'дорога', 'модель', 'партнер', 'клиент', 'доказательство']
def get_word():
    return random.choice(word_list).upper()
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = word[0] + word_completion[1:-1] + word[-1]
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    while guessed != True:
        print('Названные буквы -', *guessed_letters)
        print('Названные слова -', *guessed_words)
        print('Число ваших попыток -', tries)
        print(display_hangman(tries))
        print(word_completion)
        print('Введите букву или слово')
        letter = input().upper()
        if letter.isdigit():
            print('Дурачок, введи букву!')
        if letter in guessed_letters:
            print('Эта буква уже есть, дурачок!')
        if len(letter) == 1 and letter in word:
            guessed_letters.append(letter)
            for i in range(len(word)):
                if word[i] == letter:
                    word_completion = word_completion[:i] + letter + word_completion[i+1::]
        elif len(letter) == 1 and letter not in word:
            tries -= 1
            guessed_letters.append(letter)
        elif letter not in word:
            tries -= 1
            guessed_words.append(letter)
        elif letter == word:
            guessed = True
            print('Поздравляем, вы угадали слово! Вы победили!')
            guessed_words.append(letter)
        if '_' not in word_completion:
            guessed = True
            print('Поздравляем, вы угадали слово! Вы победили!')
        if tries == 0:
            display_hangman(tries)
            guessed = True
            print('УУУУУ, ТЫ ПРОИГРАЛ')
            print(word)
            guessed_words.append(letter)
while True:
    result = get_word()
    play(result)
    word_list.remove(result.lower())
    if len(word_list) == 0:
        print('Извините, у нас закончились слова ¯\_(ツ)_/¯')
        break
    print('Хотите сыграть еще раз?')
    answ = input()
    if answ.lower() != 'да':
        break
#замок
#__м__