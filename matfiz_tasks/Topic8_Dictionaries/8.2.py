matrixA_dict = {
    (0, 1): 5,
    (1, 4): 7,
    (2, 4): 5,
    (3, 1): -4,
    (0, 5): 1,
    (2, 1): 2
}
matrixB_dict = {
    (0, 2): 5,
    (5, 3): 7,
    (3, 4): 5,
    (3, 3): 4,
    (0, 4): 1,
    (1, 1): 2
}

rows_A, cols_A, rows_B, cols_B = 0, 0, 0, 0
for element in list(matrixA_dict.keys()):
    if element[0] + 1 > rows_A: rows_A = element[0] + 1
    if element[1] + 1 > cols_A: cols_A = element[1] + 1
for element in list(matrixB_dict.keys()):
    if element[0] + 1 > rows_B: rows_B = element[0] + 1
    if element[1] + 1 > cols_B: cols_B = element[1] + 1

for i in range(rows_A):
    for j in range(cols_A):
        if (i, j) in list(matrixA_dict.keys()): print(matrixA_dict[(i, j)], end=" ")
        else: print(0, end=" ")
    print()
print()
for i in range(rows_B):
    for j in range(cols_B):
        if (i, j) in list(matrixB_dict.keys()): print(matrixB_dict[(i, j)], end=" ")
        else: print(0, end=" ")
    print()
print()

# ---- ---- ---- task 2 ---- ---- ----
# - get the multiplication of matrices
print("--- --- Task 2: Matrices multiplication --- ---")
if cols_A == rows_B:
    rows_C, cols_C = rows_A, cols_B
    matrixC_dict = dict()
    for i in range(rows_C):
        for j in range(cols_C):
            c = 0
            for k in range(cols_A):
                a = matrixA_dict[(i, k)] if (i, k) in matrixA_dict.keys() else 0
                b = matrixB_dict[(k, j)] if (k, j) in matrixB_dict.keys() else 0
                c += a * b
            if c != 0: matrixC_dict[(i, j)] = c

    for i in range(rows_C):
        for j in range(cols_C):
            if (i, j) in list(matrixC_dict.keys()): print(matrixC_dict[(i, j)], end=" ")
            else: print(0, end=" ")
        print()
    print("\nIn dictionary format:", matrixC_dict)
else: print(" It's impossible to multiply these matrices")


# ---- ---- ---- task 3, 4 ---- ---- ----
# - get the min, max element of matrix
print("--- --- Task 3, 4: Min and max element of matrix --- ---")
min_elem = 0
max_elem = 0
for element in matrixA_dict.values():
    if element > max_elem: max_elem = element
    if element < min_elem: min_elem = element
print("Min element:", min_elem)
print("Max element:", max_elem)

# ---- ---- ---- task 6 ---- ---- ----
print("--- --- Task 6: is matrix triangular --- ---")
flag = True
for key, value in matrixA_dict.items():
    if key[0] > key[1] and value != 0:
        flag = False
        break
print("Matrix is triangular") if flag else print("Matrix is not triangular")
