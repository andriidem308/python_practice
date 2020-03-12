import numpy as np

# ndarray = np.array(object, dtype=None,
#           copy=True, order='K', sudok=False, ndmin=0)
arr_1 = np.array([1, 4, 5, 6, 2])
arr_2 = np.array([[1, 2], [3, 4]], dtype=float)
print('\nArray 1:', arr_1)
print('Array 2:', arr_2)

print('\nNum of dims 1:', arr_1.ndim)  # num of dims
print('Num of dims 2:', arr_2.ndim)
print('\nSize of array in each dimension 1:', arr_1.shape)
print('Size of array in each dimension 2:', arr_2.shape)
print('\nTotal num of elements 1:', arr_1.size)
print('Total num of elements 2:', arr_2.size)
print('\nType of elements 1:', arr_1.dtype)
print('Type of elements 2:', arr_2.dtype)

print("\na = np.array(1, 2, 3)\t# WRONG")
print("a = np.array([1, 2, 3])\t# RIGHT")

zarr = np.zeros((3, 4), dtype=float)  # array of given shape filled with zeros
oarr = np.ones((5, 5))  # array of given shape filled with ones
print('\nArray of zeros:', zarr)
print('Array of ones:', oarr)

print("\nnp.arange(10) :", np.arange(10))
print("np.arange(2, 10, dtype=float) :", np.arange(2, 10, dtype=float))
print("np.arange(2, 3, 0.2) :", np.arange(2, 3, 0.2))

print("\nnp.linspace(1., 6., 5) :", np.linspace(1., 6., 5)) # 5 -num of elements
print("np.linspace(1, 8, 8) :", np.linspace(1, 8, 8)) # 8 -num of elements

# print("np.indices((2, 3)) :", np.indices((2, 3)))

y = np.arange(35).reshape(5, 7)
# arr[np.array([a1, b1, c1]), np.array([a2, b2, c2])] ->
# -> return [ arr[a1][a2] arr[b1][b2] arr[c1][c2] ]
print('\ny:\n', y, '\nnew:\n', y[np.array([0,2,4]), np.array([0, 1, 2])])
print("y[y > 20] :", y[y > 20])
print("y[y % 5 == 0] :", y[y % 5 == 0])

x = np.arange(30).reshape(2,3,5)
print("\nx:\n", x)
b = np.array([[True, True, False], [False, True, False]])
print("new x:\n", x[b])