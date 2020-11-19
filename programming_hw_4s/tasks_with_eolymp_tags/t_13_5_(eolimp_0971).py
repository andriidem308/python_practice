n, k = map(int, input().split())

people = [_ for _ in range(1, n+1)]


i, j = 0, 0
while n > 1:
    j = (j+1) % k

    if j == 0:
        n -= 1
        people.pop(i)
    else: i = (i+1) % n

print(*people)
