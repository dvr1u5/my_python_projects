# объявление функции
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for i in range(len(txt1)):
            if txt1[i] != txt2[i]:
                count += 1
    if count == 1:
        return True
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()
# вызываем функцию
print(is_one_away(txt1, txt2))