MAX = 2147483647
MIN = -2147483648

info = tuple(map(int, input().split()))

previous = info[0]
for index in range(1, len(info)):
    current = info[index]

    if current < MIN or current > MAX:
        print("NO")
        exit()
    if current > previous: MIN = previous
    else: MAX = previous

    previous = current

print("YES")
