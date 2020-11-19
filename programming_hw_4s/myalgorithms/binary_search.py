def binary_search(array, x):
    ''' True, якщо шуканий елемент знайдено '''
    left = 0
    right = len(array) - 1
    
    while left < right:
        middle = (left + right) // 2
        
        if array[middle] < x:
            left = middle + 1
        else:
            right = middle
    
    return array[right] == x
    

def binary_search(array, x):
    ''' Повертає індекс шуканого елементу '''
    left = 0
    right = len(array) - 1
    
    while left < right:
        middle = (left + right) // 2
        
        if array[middle] < x:
            left = middle + 1
        elif array[middle] > x:
            right = middle - 1
        else:
            return middle
    
    return None
    
    
def bsearch_leftmost(array, x):
    ''' Перше входження шуканого елементу '''
    left = 0
    right = len(array)
    
    while left < right:
        middle = (left + right) // 2
        
        if array[middle] < x:
            left = middle + 1
        else:
            right = middle
        
    return left    


def bsearch_rightmost(array, x):
    ''' Останнє входження шуканого елементу '''
    left = 0
    right = len(array)
    
    while left < right:
        middle = (left + right) // 2
        
        if array[middle] <= x:
            left = middle + 1
        else:
            right = middle
    
    return left - 1