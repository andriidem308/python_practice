import shelve

f1 = shelve.open('f1')
f2 = shelve.open('f2')
g = shelve.open('g')

f1.clear()
f2.clear()
g.clear()

while True:
    key = input('Вид товару: ')
    if key == '0':
        break
    f1[key] = int(input('Кількість: '))

f1_keys = list(f1.keys())

print()

for e in f1_keys:
    f2[e] = input('{} - зміна: '.format(e))
    t = float(f1[e]) + float(f2[e])
    if t < 0: t = 0
    g[e] = t

print()

for e in f1_keys:
    print(g[e],'товарів {}-го виду'.format(e))

f1.close()
f2.close()
g.close()

