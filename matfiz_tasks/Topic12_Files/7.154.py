'''
' Created by Andrii Demchenko
' Student of 1st grade. Specialization: Computer Maths
' Task 7.154
'''

def procedure_a(f,g):
    # Opening files
    f = open('7.154_f.txt','r')
    g = open('7.154_g.txt','w')

    text  = str(f.read())

    mas = [] # temporary variable for adding indexes of '1'
    # Adding indexes and replacing '1' to '0'
    for i in range(len(text)):
        if text[i] == '1':
            mas.append(i)
            text = text[:i] + '0' + text[i+1:]

    # Replacing '0' to '1' using ex-indexes
    for i in range(len(text)):
        if text[i] == '0' and i not in mas:
            text = text[:i] + '1' + text[i+1:]

    g.write(text) # writing to out-file

def procedure_b(f,g):
    text = '' # temporary variable for adding lines
    for line in f:
        text += (line[:-1])[::-1] + '\n'

    g.write(text[:-1]) # writing to out-file

f = open('7.154_f.txt','r')
g = open('7.154_g.txt','w')

while True:
    operation = input('which operation, a or b: ')
    if operation == 'a':
        procedure_a(f,g)
        break
    if operation == 'b':
        procedure_b(f,g)
        break
    else:
        print('\nNon-correct value of operation!!!')
        

f.close()
g.close()
