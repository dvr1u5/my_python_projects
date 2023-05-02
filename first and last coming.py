string = input()
pos1 = string.find('f')
pos2 = string[::-1].find('f')
if pos1 == -1:
    print('')
elif pos1 == len(string) - pos2 - 1:
    print(pos1)
else:
    print(pos1, len(string) - pos2 - 1)
