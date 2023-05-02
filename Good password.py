# объявление функции
def is_password_good(password):
    up = False
    low = False
    digit = False
    if len(password) >= 8:
        for ch in password:
            if ch.isupper() == True:
                up = True
            if ch.islower() == True:
                low = True
            if ch.isdigit() == True:
                digit = True
    if up == True and low == True and digit == True:
        return True
    else:
        return False

# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))
