def gen(x):
    a = 1
    while True:
        yield a
        a = a + a * (-x)

n = int(input())
x = float(input())
g = gen(x)
for i in range(n):
    print(i+1,next(g))