inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
bank = {}
for i in lines:
    name = list(map(str, i.split()))
    if name[0] == 'DEPOSIT':
        bank[name[1]] = bank.get(name[1], 0) + int(name[2])
    if name[0] == 'WITHDRAW':
        bank[name[1]] = bank.get(name[1], 0) - int(name[2])
    if name[0] == 'BALANCE':
        if name[1] in bank:
            print(bank[name[1]])
        else:
            print('ERROR')
    if name[0] == 'TRANSFER':
        bank[name[2]] = bank.get(name[2], 0) + int(name[3])
        bank[name[1]] = bank.get(name[1], 0) - int(name[3])
    if name[0] == 'INCOME':
        for j in bank:
            if bank[j] > 0:
                bank[j] = int(bank.get(j, 0) +
                              (int(name[1]) / 100 * bank[j]) // 1)
