'''
' Created by Andrii Demchenko
' Student of 1st grade. Specialization: Computer Maths
' Task 7.157
'''

def procedure(f,g):
    lines = f.readlines()
    t = ''
    for i,line in enumerate(lines):
        t += str(i+1) + ' ' + line

    g.write(t)

# Opening files
f = open('7.157.txt','r')
g = open('7.157_res.txt','w')

# Doing procedure
procedure(f,g)

# Closing files
f.close()
g.close()
