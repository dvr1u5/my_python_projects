import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', '	Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос')
print('Как вас зовут?')
name = input()
print('Привет', name)
while True:
    print('Задайте мне вопрос и я отвечу :)')
    question = input()
    answer = random.choice(answers)
    print('Хотите ли вы задать еще один вопрос? Да / нет')
    answer2 = input()
    if answer2.lower() == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
