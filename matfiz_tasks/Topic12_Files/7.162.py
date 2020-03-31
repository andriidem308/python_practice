'''
' Created by Andrii Demchenko
' Student of 1st grade. Specialization: Computer Maths
' Task 7.162
'''

def procedure(f,g):
    mas = f.readlines()
    t = ''
    for i in range(len(mas)):
        mas[i] = mas[i].split()
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if int(mas[i][j]) > 0:
                t += mas[i][j] + ' '
    g.write(t)
                
# Opening files
f = open('7.162.txt','r')
g = open('7.162_res.txt','w')

# Doing main procedure
procedure(f,g)

# Closing files
f.close()
g.close()
