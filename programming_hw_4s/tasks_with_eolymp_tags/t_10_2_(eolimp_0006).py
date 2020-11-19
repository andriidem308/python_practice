d = [0] * 15
c = [0] * 15
max_profit = 0


def procedure(k, mp):
    global d, c, max_profit

    cur_d = 0
    for j in range(n):
        if d[j] >= k:
            tmp = (d[j] - k + 1) * c[j]
            cur_d, d[j] = d[j], 0
            procedure(k + 1, mp + tmp)
            d[j], cur_d = cur_d, 1

    if cur_d == 0 and mp > max_profit: max_profit = mp


n = int(input())
for i in range(n): d[i], c[i] = map(int, input().split())

procedure(1, 0)

print(max_profit)
