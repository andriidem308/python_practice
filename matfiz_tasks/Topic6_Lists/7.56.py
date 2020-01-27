vector_b = list(map(float, input("Enter Vector B: ").split()))

# Honestly, for successful multiplication matrix A
# must have only one column so we can input it in one line
matrix_a = list(map(float, input("Enter Matrix A by rows: ").split()))

# So, we know that size of NxM * MxK matrix will be NxK
rows = len(matrix_a)
cols = len(vector_b)
result = []
for i in range(rows):
    result.append([])
    for j in range(cols):
        result[i].append(matrix_a[i] * vector_b[j])

print("\nMultiplication of matrices: ")
for row in result:
    for col in row:
        print(col, end=" ")
    print()
