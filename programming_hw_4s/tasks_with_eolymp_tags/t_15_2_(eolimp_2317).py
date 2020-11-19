class Tree:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def has_children(self):
        return bool(self.children)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_child(self, key):
        for child in self.children:
            if child.key == key:
                return child

    def dfs(self, key):
        queue = [self]

        while queue:
            node = queue.pop(0)

            if node.key == key: return node
            for child in node.children: queue.append(child)

    def add(self, parent_key, child_key):
        parent = self.dfs(parent_key)
        parent.add_child(Tree(child_key))

    def get(self, i, j):
        node_a = self.dfs(i)
        node_b = self.dfs(j)

        while True:
            while node_b.key >= node_a.key:
                if node_a is node_b: return node_a.key
                node_b = node_b.parent

            node_a = node_a.parent

    def procedure(self, cmd):
        cmd = cmd.split()
        name = cmd[0].lower()
        args = map(int, cmd[1:])

        return getattr(self, name)(*args)


tree = Tree(1)

k = int(input())
for _ in range(k):
    result = tree.procedure(input())
    if result: print(result)