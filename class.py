from sys import stdin


class Matrix:
    def __init__(self, Mlist):
        self.Mlist = [line.copy() for line in Mlist]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.Mlist])

    def size(self):
        return len(self.Mlist), len(self.Mlist[0])

exec(stdin.read())
