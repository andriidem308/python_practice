from math import sqrt, cos, pi


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Point2Ex(Point2):
    def __init__(self, x, y):
        Point2.__init__(self, x, y)

    def equal(self, A):
        if self.x == A.x and self.y == A.y:
            return True
        else:
            return False


class Segment:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self) -> object:
        return self._b

    def __str__(self):
        return "[{}, {}]".format(self._a, self._b)

    def len(self):
        return sqrt((self._a.get_x() - self._b.get_x()) ** 2 +
                    (self._a.get_y() - self._b.get_y()) ** 2)


class SegmentEx(Segment):

    def __init__(self, _a, _b):
        Segment.__init__(self, _a, _b)

    def equal(self, obj2):
        if self.len() == obj2.len():
            return True
        else:
            return False


def EqualSegments(segments):
    length = segments[0].len()
    res = True
    for el in segments:
        if el.len() != length:
            res = False
            break
    return res


def HasSimilarPoint(seg1, seg2):
    if seg1._a == seg2._a: return True
    if seg1._a == seg2._b: return True
    if seg1._b == seg2._a: return True
    if seg1._b == seg2._b: return True
    return False


def IsPolygon(segments):
    if not EqualSegments(segments): return False
    segs = []
    t = 0
    for i in range(len(segments)):
        if segments[i] not in segs:
            for j in range(len(segments)):
                if i != j:
                    if HasSimilarPoint(segments[i], segments[j]):
                        segs.append(segments[j])
                        print((segments[i]._a, segments[i]._b), (segments[j]._a, segments[j]._b))
                        segs.append(segments[i])
    if len(segs) == len(segments): return True
    return False


def IsPolygon(segments):
    point = segments[0]._a
    segs = [segments[0]]
    for j in range(len(segments)):
        for i in range(len(segments)):
            if segments[i] not in segs:
                if point.equal(segments[i]._a):
                    point = segments[i]._b
                    segs.append(segments[i])
                if point.equal(segments[i]._b):
                    point = segments[i]._a
                    segs.append(segments[i])
        if point.equal(segments[0]._b):
            return True
    return False


def IsRegularPolygon(segments):
    if EqualSegments(segments) and IsPolygon(segments):
        return True
    else:
        return False


n = int(input('n: '))
lst = []
for i in range(n):
    x1 = float(input('x1: '))
    y1 = float(input('y1: '))
    x2 = float(input('x2: '))
    y2 = float(input('y2: '))
    a = Point2Ex(x1, y1)
    b = Point2Ex(x2, y2)
    seg = SegmentEx(a, b)
    lst.append(seg)

print(IsPolygon(lst))
print(IsRegularPolygon(lst))

A = SegmentEx(Point2Ex(0,0),Point2Ex(2,0))
B = SegmentEx(Point2Ex(0,0),Point2Ex(2,3))