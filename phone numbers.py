phonenumber = ''.join(filter(str.isdigit, input()))
numbers = {}
if ('7' == phonenumber[0] or '8' == phonenumber[0]) and len(phonenumber) > 7:
    phonenumber = phonenumber[1::]
if len(phonenumber) == 7:
    phonenumber = '495' + phonenumber
for i in range(3):
    num = ''.join(filter(str.isdigit, input()))
    if ('7' == num[0] or '8' == num[0]) and len(num) > 7:
        num = num[1::]
    if len(num) == 7:
        num = '495' + num
    numbers[i] = num
    if phonenumber == numbers[i]:
        print('YES')
    else:
        print('NO')
