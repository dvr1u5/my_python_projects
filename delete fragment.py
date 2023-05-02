string = input()
pos1 = string.find('h')
pos2 = string[::-1].find('h')
d = string[0:pos1]
a = string[len(string) - pos2::]
print(d, a, sep='')
