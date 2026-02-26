def solution(n, k, cmd):
    class Node:
        def __init__(self, id):
            self.id = id
            self.left = None
            self.right = None

    nodes = [Node(i) for i in range(n)]
    for i in range(1, n):
        nodes[i].left = nodes[i-1]
        nodes[i-1].right = nodes[i]

    cur = nodes[k]
    removed = []

    for c in cmd:
        if c[0] == 'U':
            x = int(c.split()[1])
            for _ in range(x):
                cur = cur.left

        elif c[0] == 'D':
            x = int(c.split()[1])
            for _ in range(x):
                cur = cur.right

        elif c[0] == 'C':
            removed.append(cur)
            if cur.left:
                cur.left.right = cur.right
            if cur.right:
                cur.right.left = cur.left
            cur = cur.right if cur.right else cur.left

        elif c[0] == 'Z':
            node = removed.pop()
            if node.left:
                node.left.right = node
            if node.right:
                node.right.left = node

    answer = ['X'] * n
    node = cur
    while node.left:
        node = node.left
    while node:
        answer[node.id] = 'O'
        node = node.right

    return ''.join(answer)