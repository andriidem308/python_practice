'''
'   Task #7.13
'   Created by Andrii Demchenko
'   Computer Mathematics, 1st grade
'
'   Скласти програми (свій пункт, я зробив 4)
'   а) всі голосні літери, які входять до кожного слова;
'   б) всі приголосні літери, які не входять до жодного слова;
'   ж) всі дзвінки приголосні літери, які входять
'      в кожне непарне слово і не входять в жодне парне слово;
'   з) всі глухі приголосні літери, які входять хоча б
'      в одне непарне слово та невходять в жодне парне слово.
'''

vowels = {'а','о','у','и','і','ї','є','я','ю','е'}
consonants = {'б','в','г','ґ','д','ж','з','й','к',
             'л','м','н','п','р','с','т','ф',
             'х','ц','ч','ш','щ','ь'}
ringing_consonants = {'б','г','ґ','д','ж','з','дз',
                      'дж','в','л','м','н','р','й'}
deaf_consonants = {'п','х','т','с','ч','ц','ф'}


text = 'З дороги було видно, як вився' + \
      ' у низині кривульками глибокий та каламутний Прут.'
txt = ''.join(text[:-1].split(','))

txt = txt.split()

#а
for i in range(len(txt)):
    letterset = set()
    for e in txt[i]:
        if e in vowels:
            letterset.add(e)
    print(letterset, 'from:', txt[i])

#б
print()
missing_consonants = set()
for e in consonants:
    if e not in text:
        missing_consonants.add(e)
print(missing_consonants)

#ж
print()
ringings_set = set()
for i in range(len(txt)-1):
    for e in consonants:
        if (e in txt[i] and e not in txt[i+1] and i%2==1):
            ringings_set.add(e)
print(ringings_set)

#з
print()
deaf_set = set()
for i in range(len(txt)-1):
    for e in consonants:
        if (e in txt[i] and e not in txt[i+1] and i%2==0):
            deaf_set.add(e)
print(deaf_set)   
