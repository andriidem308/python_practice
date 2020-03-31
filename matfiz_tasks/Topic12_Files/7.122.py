'''
' Created by Andrii Demchenko
' Student of 1st grade. Specialization: Computer Maths
' Task 7.122
'''

# Files openning
f = open('7.122.txt','r')
f_s = open('7.122_s.txt','r')
f_res = open('7.122_res.txt','w')

# Declaring variables
s = int(f_s.read()[0])
lines = f.readlines()
mas = []

# Adding symbols to output massive
for e in lines[s-1]:
    mas += e

# Adding massive to out-file without
# external brackets of massive
f_res.write(str(mas[:-1])[1:-1])

# Closing files
f.close()
f_s.close()
f_res.close()



