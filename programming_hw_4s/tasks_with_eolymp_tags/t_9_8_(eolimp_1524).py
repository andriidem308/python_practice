MAX_SIZE = 71
MAX_NUMBER = 2**32

matrix = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

for i in range(MAX_SIZE):
    matrix[i][0] = 1
    matrix[1][i] = 1

for i in range(2, MAX_SIZE):
    for j in range(1, MAX_SIZE):
        sum = matrix[i][j-1] + matrix[i-1][j]
        matrix[i][j] = sum if sum < MAX_NUMBER else MAX_NUMBER

k = int(input())
for i in range(k):
    n, t, p = map(int, input().split())
    t -= n * p
    print(matrix[n][t])


