'-----------------------------------------------------------------------------'
#================================___ФУНКЦІЇ___================================
#Функція із рекурсією
def golden_pyramid(triangle, row=0, column=0, total=0):    
    if row == len(triangle) - 1:
        return total + triangle[row][column]
    return max(golden_pyramid(triangle, row + 1, column,\
                total + triangle[row][column]),\
                golden_pyramid(triangle, row + 1, column + 1,\
                total + triangle[row][column]))

#Функція без рекурсії
def golden_pyramid_d(triangle):
    sums = [row[:] for row in triangle]
    for i in range(len(sums) - 2, -1, -1):
        for j in range(i + 1):
            sums[i][j] += max(sums[i + 1][j],\
            sums[i + 1][j + 1])
    return sums[0][0]

#=============================================================================
'-----------------------------------------------------------------------------'



'*****************************************************************************'
#=======================___ОСНОВНА_ЧАСТИНА_ПРОГРАМИ___========================

n = int(input('input n = '))
lst = []
for i in range(n):
    lst.append([])
    lst[i] = list(map(int,input('Уведіть %d'%(i+1)+'-й рядок: ').split()))

golden_pyramid_main = [row[:] for row in lst]
for i in range(len(golden_pyramid_main) - 2, -1, -1):
    for j in range(i + 1):
        golden_pyramid_main [i][j] += \
        max(golden_pyramid_main[i + 1][j],golden_pyramid_main[i + 1][j + 1])
        
#=============================================================================
'*****************************************************************************'

'-----------------------------------------------------------------------------'
#===============================___ВИВЕДЕННЯ___===============================

#---СУМИ---

print('\nСума = ', golden_pyramid(lst,row=0,column=0,total=0))  #Через рекурсивну функцію
print('Сума = ', golden_pyramid_d(lst))                         #Через нерекурсивну функцію
print('Сума = ', golden_pyramid_main[0][0])                     #Без використання надбудов

#---ПІРАМІДА---

print('\nПіраміда: ')
for i in range(n):
    s = (n-i)*' ' + ' '*6   #Для оформлення
    for j in range(i+1):
        s += str(lst[i][j])+' '
    print(s)
print('========END=========')

#=============================================================================
'-----------------------------------------------------------------------------'
