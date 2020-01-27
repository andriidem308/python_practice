import numpy as np

# some_matrix = np.array([
#       [*elements_1],
#       .  .  .  .  .
#       [*elements_n],
# ])

""" 0. Matrix Example: """
matrix = np.array([['Mon', 18, 20, 22, 17],
                   ['Tue', 11, 18, 21, 18],
                   ['Wed', 15, 21, 20, 19],
                   ['Thu', 11, 20, 22, 21],
                   ['Fri', 18, 17, 23, 22],
                   ['Sat', 12, 22, 20, 18],
                   ['Sun', 13, 15, 19, 16]])
print("\n--- Matrix: ---")
print(matrix, "\n")

# matrix_r = np.reshape(arr, (7, 5))

""" 1. Accessing values in a matrix """
print(matrix[2])  # print data for Wednesday
print(matrix[3][1])  # print data for Thursday morning
print(matrix[5][3])  # print data for Saturday evening

""" 2. Adding a row / column """
# m_r = np.append(matrix, [['Avg', 12, 15, 13, 11]], 0)                   # adding a row (to the end)
m_r = np.insert(matrix, 7, [['Avg', 14, 19, 21, 18]], 0)  # adding a row
m_c = np.insert(matrix, 5, [1, 2, 3, 4, 5, 6, 7], 1)  # adding a column

print("\nRow <Avg> added:\n", m_r)  # adding row <Avg> with
print("\nColumn <1..7> added:\n", m_c)

""" 3. Delete a row / column """
m_rd = np.delete(matrix, 2, axis=0)
m_cd = np.delete(matrix, 2, axis=1)

print("\nRow <Wed> deleted:\n", m_rd)
print("\nColumn <20,..,15> deleted:\n", m_cd)

""" 4. Update a row in a Matrix """
m_ru = matrix
m_ru[3] = ["Thu", 0, 0, 0, 0]
print("\nRow <Thu> updated:\n", m_ru)



