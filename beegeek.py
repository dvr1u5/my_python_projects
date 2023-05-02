# объявление функции
import math
def is_valid_password(password):
    flag1 = False
    flag2 = False
    flag3 = False
    if len(password) == 3:
        for i in range(1, len(password)):
            password[i] = int(password[i])
        if password[0] == password[0][::-1]:
            flag1 = True
        i = password[1]
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                break
            j += 1
        else:
            flag2 = True
        if password[2] % 2 == 0:
            flag3 = True
        print(flag1, flag2, flag3)
        if flag1 == True and flag2 == True and flag3 == True:
            return True
        else:
            return False
    else:
        return False
# считываем данные
psw = input()
psw2 = psw.split(':')
# вызываем функцию
print(is_valid_password(psw2))
