class UpIterator:
    def __init__(self, data):
        self._data = sorted(data)
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._data) - 1:
            raise StopIteration
        self._index = self._index + 1
        return self._data[self._index]


class DownIterator(UpIterator):
    def __init__(self, data):
        UpIterator.__init__(self, data)
        self._index = len(data)

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index = self._index - 1
        return self._data[self._index]


"""
seq = list(map(int,input().split()))
toup = sorted(seq)
todown = toup[::-1]

oper = int(input('1 - Зростання\n2 - Спадання:\n'))
if oper == 1:
    itr = iter(toup)
elif oper == 2:
    itr = iter(todown)
else:
    raise ValueError("Неправильне значення. Уведіть 1 чи 2!!!")

for i in range(len(seq)):
    print(next(itr))

print(seq, ' - seq НЕ змінюється!')
"""

seq = list(map(int,input().split()))
itr = UpIterator(seq)
for i in range(len(seq)):
    print(next(itr))
print()
itr = DownIterator(seq)
for i in range(len(seq)):
    print(next(itr))
