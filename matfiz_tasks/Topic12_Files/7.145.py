import shelve

f = shelve.open('f145')
f.clear()

while True:
    key = input('Назва іграшки: ')
    if key == '0':
        break
    f[key] = input('Вартість / Вік від / Вік до ').split()

namelist = list(f.keys())
toys = []
summ = 0
for el in namelist:
    if len(toys) == 2 or summ > 20:
        break
    else:
        if int(f[el][1]) <= 3 and int(f[el][2]) >= 3 \
           and summ + float(f[el][0]) <= 20:
            toys.append(f[el])
            summ += float(f[el][0])

print(toys)
print(summ)
     
    

f.close()
