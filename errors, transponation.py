from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Mlist2, Mlist3):
        self.matrix1 = Mlist2
        self.matrix2 = Mlist3


class Matrix:
    def __init__(self, Mlist):
        self.Mlist = deepcopy(Mlist)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.Mlist])

    def size(self):
        return len(self.Mlist), len(self.Mlist[0])

    def __add__(self, NewMlist):
        if len(self.Mlist) != len(NewMlist.Mlist):
            raise MatrixError(self, NewMlist)
        else:
            Mlist2 = list()
            for j in range(len(self.Mlist)):
                l = list(map(
                    lambda a, b: a + b, self.Mlist[j], NewMlist.Mlist[j]))
                Mlist2.append(l)
            return Matrix(Mlist2)

    def transpose(self):
        self.Mlist = list(zip(*self.Mlist))
        return Matrix(self.Mlist)

    def transposed(self):
        return Matrix(list(zip(*self.Mlist)))

    def __mul__(self, numint):
        Mlist3 = list()
        for j in range(len(self.Mlist)):
            l = list(i * numint for i in self.Mlist[j])
            Mlist3.append(l)
        return Matrix(Mlist3)
    __rmul__ = __mul__

exec(stdin.read())
