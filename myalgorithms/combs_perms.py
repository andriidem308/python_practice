
def permute(alist):
    if len(alist) <= 1:
        yield alist
        alist = []

    for s in alist:
        rest = list(alist[:])
        rest.remove(s)
        for p in permute(rest):
            yield [s] + p

def choosenk(alist, n):
    if len(alist) <= n:
        yield alist
        alist = []

    if alist:
        head = alist[0]
        rest = list(alist[1:])
        for c in choosenk(rest, n-1):
            yield [head] + c
        for c in choosenk(rest, n):
            yield c


def test_permute(lst):
    print('\n%s permute(%s):' % ('-' * 20, lst))
    for p in permute(lst):
        print(p)


def test_chosenk(lst, n):
    print('\n%s choosenk(%s, %d):' % ('-' * 20, lst, n))
    for c in choosenk(lst, n):
        print(c)


test_permute([1,2,3,4])
test_permute('abc')
test_permute('')
test_permute([1])

test_chosenk([1,2,3,4], 2)
test_chosenk('abc', 2)
test_chosenk('abc', 1)
test_chosenk('abc', 0)
test_chosenk('a', 2)
test_chosenk('', 2)