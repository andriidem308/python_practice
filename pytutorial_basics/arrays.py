from array import *


def arr_print(_array: array):
    for element in _array: print(element, end=' ')
    print()


# some_array = array(typecode, [Initializers])
# typecode: b - signed integer of size 1 byte;
#           B - unsigned integer of size 1 byte;
#           c - character of size 1 byte;
#           i - signed integer of size 2 bytes;
#           I - unsigned integer of size 2 bytes;
#           f - floating point of size 4 bytes;
#           d - floating point of size 8 bytes;
# Example:
arr = array('i', [4, 3, 7, 10, 5, 2, 9])

''' 0. output all array's elements'''
print("\nOriginal array:", end=' ')
for x in arr: print(x, end=' ')
print()

''' 1. accessing element with index <4> in <arr> '''
print("\nArray:", end=' ')
arr_print(arr)
print("Element of index <4> -", arr[4])

''' 2. insert element with value <11> into index  <5> in <arr> '''
print("\nArray BEFORE insertion:\t", end=' ')
arr_print(arr)
arr.insert(5, 11)
print("Array AFTER insertion:\t", end=' ')
arr_print(arr)

''' 3. remove first element with value <3> in <arr> '''
print("\nArray BEFORE removing:\t", end=' ')
arr_print(arr)
arr.remove(3)
print("Array AFTER removing:\t", end=' ')
arr_print(arr)

''' 4. return first element with value <10> in <arr> '''
print("\nArray:", end=' ')
arr_print(arr)
print("First element with value <10> -", arr.index(10))

''' 5. update element of index <1> with value <12> in <arr> '''
print("\nArray BEFORE updating:\t", end=' ')
arr_print(arr)
arr[1] = 12
print("Array AFTER updating:\t", end=' ')
arr_print(arr)
print()

