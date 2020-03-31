class Multiset:
    dictionary = None
    multiset = None

    def __init__(self):
        self.dictionary = dict()
        self.multiset = set()

    def __str__(self):
        s = ''
        for e in self.dictionary.keys():
            s += str(e) + ' : ' + str(self.dictionary[str(e)]) + '\n'
        return s

    def makeClear(self):
        self.multiset = set()
        self.dictionary = dict()

    def isClear(self):
        return True if self.multiset == set() else False

    def __add__(self, other):
        try:
            assert str(other) in self.dictionary.keys() and other in self.multiset
            self.dictionary[other] += 1
        except AssertionError:
            self.multiset.add(other)
            self.dictionary[str(other)] = 1

    def __remove__(self,other):
        try:
            assert str(other) in self.dictionary.keys() and other in self.multiset
            self.dictionary[str(other)] -= 1
            if self.dictionary[str(other)] == 0:
                del self.dictionary[str(other)]
                self.multiset.remove(str(other))
        except AssertionError:
            print('Multiset has not this element')
        except KeyError:
            print('Dict has not element with this key')

    def howMany(self,elem):
        return self.dictionary[str(elem)]

    def splitOther(self, other):
        res = Multiset()
        res.multiset.update(self.multiset, other.multiset)
        for el in res.multiset:
            if str(el) in self.dictionary.keys() and str(el) in other.dictionary.keys():
                res.dictionary[str(el)] = max(self.dictionary[str(el)], other.dictionary[str(el)])
            elif str(el) in self.dictionary.keys():
                res.dictionary[str(el)] = self.dictionary[str(el)]
            elif str(el) in other.dictionary.keys():
                res.dictionary[str(el)] = other.dictionary[str(el)]
        return res

    def intersectOther(self, other):
        res = Multiset()
        res.multiset = self.multiset.intersection(other.multiset)
        for el in res.multiset:
            if str(el) in self.dictionary.keys() and str(el) in other.dictionary.keys():
                res.dictionary[str(el)] = min(self.dictionary[str(el)], other.dictionary[str(el)])
            elif str(el) in self.dictionary.keys():
                res.dictionary[str(el)] = self.dictionary[str(el)]
            elif str(el) in other.dictionary.keys():
                res.dictionary[str(el)] = other.dictionary[str(el)]
        return res


S1 = Multiset()
S2 = Multiset()
s1 = input('s1: ')
s2 = input('s2: ')

for w in s1:
    S1.__add__(w)
for w in s2:
    S2.__add__(w)

S = S1.intersectOther(S2)
print('First statement:', S1.dictionary == S2.dictionary)
print('Second statement:', S1.dictionary == S.dictionary)

