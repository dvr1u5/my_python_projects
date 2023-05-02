# объявление функции
def is_palindrome(text):
    if s1.lower() == s1[::-1].lower():
        return True
    else:
        return False
# считываем данные
txt = input()
s1 = "".join(c for c in txt if c.isalpha())
# вызываем функцию
print(is_palindrome(txt))
