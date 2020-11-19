global tree, colours, result


def dfs(v):
    current = {colours[v]}

    for j in range(len(tree[v])):
        tmp = dfs(tree[v][j])
        if len(current) < len(tmp):
            current, tmp = tmp, current

        for t in tmp: current.add(t)
        del tmp

    result[v] = len(current)
    return current


if __name__ == "__main__":
    n = int(input())

    tree = [[] for _ in range(n)]
    colours = [0] * n
    result = [0] * n
    root = 1

    for i in range(n):
        p, c = map(int, input().split())
        colours[i] = c

        if p == 0: root = i
        else:
            tree[p - 1].append(i)

    dfs(root)
    print(*result)
