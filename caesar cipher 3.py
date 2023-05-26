line = input()
lenght = 0
i = 0

def lenght_of_word(line, j):
    lenght = 0
    while line[j].isalpha():
        lenght += 1
        j += 1
    return lenght

while i < len(line):
    if line[i].isalpha():

    print(lenght_of_word(line, i))
    i += 1


