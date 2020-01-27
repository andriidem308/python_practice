from math import atan, pi


def arctan(_x, _y):
    if (_x > 0) and (_y > 0): return pi / 2
    elif (_x < 0) and (_y < 0): return -pi + atan(_x / _y)
    elif (_x < 0) and (_y == 0): return -pi / 2
    elif (_x >= 0) and (_y < 0): return pi + atan(_x / _y)
    elif _y > 0: return atan(_x / _y)


print(arctan(2, 2))
print(arctan(-2, -2))
print(arctan(-13, 44))
