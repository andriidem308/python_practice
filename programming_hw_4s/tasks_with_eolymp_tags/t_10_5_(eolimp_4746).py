n = int(input())

if n:
    arr = sorted([int(x) for x in input().split()], reverse=True)
    print(sum(max(x-i, 0) for i, x in enumerate(arr)))
else:
    print(0)