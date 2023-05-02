string = input()
pos1 = string.find('h')
pos2 = string[::-1].find('h')
fragment = string[pos1 + 1:]
out = string[:(len(string) - pos2 - 1)]
print(out + fragment)
