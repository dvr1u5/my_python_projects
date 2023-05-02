from sys import stdin


class Matrix:
    def __init__(self, Mlist):
        self.Mlist = [line.copy() for line in Mlist]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.Mlist])

    def size(self):
        return len(self.Mlist), len(self.Mlist[0])

    def __add__(self, NewMlist):
        Mlist2 = list()
        for j in range(len(self.Mlist)):
            l = list(map(lambda a, b: a + b, self.Mlist[j], NewMlist.Mlist[j]))
            Mlist2.append(l)
        return Matrix(Mlist2)

    def __mul__(self, numint):
        Mlist3 = list()
        for j in range(len(self.Mlist)):
            l = list(i * numint for i in self.Mlist[j])
            Mlist3.append(l)
        return Matrix(Mlist3)
    __rmul__ = __mul__

exec(stdin.read())
