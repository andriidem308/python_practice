'''
' Created by Andrii Demchenko
' Student of 1st grade. Specialization: Computer Maths
' Task 7.125
'''

# f1 -> h
f1 = open('7.125_1.txt', 'r')
h  = open('7.125_h.txt', 'w')
h.write(f1.read())
h.close()
f1.close()

# f2 -> f1
f1 = open('7.125_1.txt', 'w')
f2 = open('7.125_2.txt', 'r')
f1.write(f2.read())
f1.close()
f2.close()

# h -> f2
h  = open('7.125_h.txt', 'r')
f2 = open('7.125_2.txt', 'w')
f2.write(h.read())
f2.close()
h.close()




