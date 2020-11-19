global tree, colours, stack, result


def dfs(v):
    global tree, colours, stack, result

    current_colour = colours[v]

    if not stack[current_colour]: result[v] = -1
    else: result[v] = stack[current_colour][-1]

    stack[current_colour].append(v)

    for itr in range(len(tree[v])):
        subtree = tree[v][itr]
        dfs(subtree)

    stack[current_colour].pop()


if __name__ == "__main__":
    n, c = map(int, input().split())
    parents = list(map(int, input().split()))
    colours_numbers = list(map(int, input().split()))

    tree = [[] for _ in range(n + 1)]
    stack = [[] for _ in range(n + 1)]
    colours = [0] * (n + 1)
    result = [0] * (n + 1)

    for i in range(2, n + 1):
        for j in parents:
            tree[j].append(i)
            parents.pop(0)
            break

    for i in range(1, n + 1):
        colours[i] = colours_numbers[i - 1]

dfs(1)
print(*result[1:])
