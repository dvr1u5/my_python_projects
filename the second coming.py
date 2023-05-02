string = input()
pos1 = string.find('f')
pos2 = string[pos1+1:].find('f')
if pos1 == -1:
    print(-2)
elif pos2 == -1:
    print(-1)
else:
    print(pos2+pos1+1)
