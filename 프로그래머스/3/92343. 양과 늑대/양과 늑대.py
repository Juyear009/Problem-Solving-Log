def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)

    answer = 0

    def dfs(sheep, wolf, possible):
        nonlocal answer
        answer = max(answer, sheep)

        for node in possible:
            ns = sheep
            nw = wolf

            if info[node] == 0:
                ns += 1
            else:
                nw += 1

            if nw >= ns:
                continue

            new_possible = possible.copy()
            new_possible.remove(node)
            new_possible += tree[node]

            dfs(ns, nw, new_possible)

    dfs(1, 0, tree[0])
    return answer