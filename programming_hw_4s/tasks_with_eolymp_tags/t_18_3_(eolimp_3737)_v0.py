n = int(input())
numbers = [0] + list(map(int, input().split()))
flag = True

for i in range(1, n//2+1):
    if (2 * i <= n and numbers[i] > numbers[2 * i]) or (2 * i + 1 <= n and numbers[i] > numbers[2 * i + 1]):
        flag = False
        break

print("YES" if flag else "NO")