number = input().split('-')
if number[0] == '7':
    number.remove('7')
if len(number[0]) == 3 and len(number[1]) == 3 and len(number[2]) == 4:
    for i in number:
        if i.isdigit() == False:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')
print(number)