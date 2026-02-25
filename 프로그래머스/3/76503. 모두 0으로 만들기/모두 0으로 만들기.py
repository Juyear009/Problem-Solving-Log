def solution(a, edges):
    def dfs():
        cnt = 0
        stack = [[0,-1,False]]
        while stack:
            node,root,check = stack.pop()
            if not check:
                stack.append([node,root,True])
                for newNode in graph[node]:
                    if newNode != root:
                        stack.append([newNode,node,False])
            elif check:
                for newNode in graph[node]:
                    if newNode != root:
                        cnt += abs(dp[newNode])
                        if dp[newNode] < 0:
                            dp[node] += dp[newNode]
                        else:
                            dp[node] += dp[newNode]
                        dp[newNode] = 0
                dp[node] += a[node]
        return cnt
                
    answer = -2
    graph = [[] for _ in range(len(a))]
    dp = [0] * len(a)
    for v,w in edges:
        graph[v].append(w)
        graph[w].append(v)
    
    answer = dfs()
    if dp[0] != 0:
        answer = -1
        
    return answer


