from array import array

# 2-dimensional array initialization
arr2dim = [[11, 12, 5, 2],
           [15, 6, 10],
           [10, 8, 12, 5],
           [12, 15, 8, 6]]

# insertion <13> at pos <3> into a row with index <1>
arr2dim[1].insert(3, 13)

# printing 2d-array
for arr in arr2dim:
    for element in arr:
        print(element, end=" ")
    print()


