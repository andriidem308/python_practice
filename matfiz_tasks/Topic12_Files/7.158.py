'''
' Created by Andrii Demchenko
' Student of 1st grade. Specialization: Computer Maths
' Task 7.158
'''

# Openning files
f     = open('7.158.txt','r')
f_s   = open('7.158_s.txt','r')
f_res = open('7.158_res.txt','w')

# Declaring variables
s = f_s.readline()
str_mas = []
lines = f.readlines()

# Adding finding lines to massive
for i,e in enumerate(lines):
    if s in e:
        str_mas.append(str(i+1) + ' line - ' + e)

# Adding string result to file
res = ''
for t in str_mas:
    res += t
f_res.write(res)

# Closing files
f.close()
f_s.close()
f_res.close()
