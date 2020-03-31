'''
'   Task #7.8
'   Created by Andrii Demchenko
'   Computer Mathematics, 1st grade
'
'   Скласти програми
'   а) обчислення кількості різних (значущих)
'      цифр у десятковому записі натурального числа n;
'   б) друку у порядку зростання всіх цифр, які не
'      входять до десяткового запису натурального числа n.
'   
'''

n = int(input('n: '))
figures = {0,1,2,3,4,5,6,7,8,9}
st = set()
m = int(n)

while m > 0:
    st.add(m % 10)
    m //= 10

#а
print(len(st), '- amount of different figures of number n')

#б
figures.difference_update(st)
print(figures, '- figures which are not in our number')

