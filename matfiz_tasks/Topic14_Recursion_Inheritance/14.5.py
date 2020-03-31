import numpy


class Matrix(object):
    def __init__(self, mat):
        self.mat = mat
        self.row = len(mat)
        self.col = len(mat[0])
        self._matRes = []
        self.__s = ''

    def __str__(self):
        self.__s = ''
        for i in range(self.row):
            self.__s += '\n'
            for j in range(self.col):
                self.__s += '%g\t' % (self.mat[i][j])
        return self.__s

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(self.row):
                for j in range(self.col):
                    self.mat[i][j] *= other
            return Matrix(self.mat)

        if self.col != other.row: return 'The number of columns of the first matrix must be equal to the number of rows of the second.'
        self._matRes = [[0 for r in range(other.col)] for c in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(other.row):
                    self._matRes[i][j] += self.mat[i][k] * other.mat[k][j]
        return Matrix(self._matRes)

    def __add__(self, other):
        if not (self.row == other.row) and (
                self.col == other.col): return 'The number of col is not equal to the number of row'
        self._matRes = [[0 for r in range(self.col)] for c in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self._matRes[i][j] += self.mat[i][j] + other.mat[i][j]
        return Matrix(self._matRes)

    def __pow__(self, other):
        if not isinstance(other, int): return 'only int'
        if other == 0: return 'Prime matrix'
        if other < 0: return 'only int'
        for i in range(1, other + 1):
            if i != other:
                self.__s += 'matrix(self.mat)*'
            else:
                self.__s += 'matrix(self.mat)'
        return eval(self.__s)

    def __min__(self):
        m = self.mat[0][0]
        for r in self.mat:
            for e in r:
                if e < m: m = e
        return m

    def __max__(self):
        m = self.mat[0][0]
        for r in self.mat:
            for e in r:
                if e > m: m = e
        return m

    def SetElement(self,other):
        keys = list(other.keys())
        values = list(other.values())
        for i in range(len(keys)):
            t = tuple(keys[i])
            r = t[0]
            c = t[1]
            self.mat[r][c] = values[i]


def getSize(dictionary):
    keys = list(dictionary.keys())
    rows = keys[0][0]
    cols = keys[0][1]
    for el in keys:
        if el[0] > rows: rows = el[0]
        if el[1] > cols: cols = el[1]
    return [rows+1, cols+1]


def makeZeroMatrix(m,n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            mat[i].append(0)
    return mat

dictionary1 = {(1, 2): 5, (0, 4): 1, (0, 5): 7}
size1 = getSize(dictionary1)
dictionary2 = {(1, 3): 5, (1, 3): 1, (5, 2): 7}
size2 = getSize(dictionary2)


M = Matrix(makeZeroMatrix(size1[0],size1[1]))
M1 = Matrix(makeZeroMatrix(size2[0],size2[1]))
M.SetElement(dictionary1)
M1.SetElement(dictionary2)

print(M)
print(M1)

print('\n----------------------\nМатриця-1 x Матриця-2:')
print(M.__mul__(M1))
print('----------------------')

