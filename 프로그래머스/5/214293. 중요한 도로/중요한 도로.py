import heapq

def solution(n, roads):
    def dijkstra(start):
        hq = [[0,start]]
        dists = [float('inf')] * (n+1)
        dists[start] = 0
        while hq:
            curDist,curNode = heapq.heappop(hq)
            if dists[curNode] < curDist:
                continue
            for newNode,length,traffic in graph[curNode]:
                if dists[newNode] > curDist + length + traffic:
                    dists[newNode] = curDist + length + traffic
                    heapq.heappush(hq,[curDist+length+traffic,newNode])
        return dists
            
    graph = [[] for _ in range(n+1)]
    edges = []
    idx = 1
    for u,v,l,t in roads:
        graph[u].append([v,l,t])
        graph[v].append([u,l,t])
        edges.append([u,v,l,t,idx])
        idx += 1
        
    distStart = dijkstra(1)
    distEnd = dijkstra(n)
    minDist = distStart[n]
    answer = set()
    
    dag = [[] for _ in range(n+1)]
    reverseDag = [[] for _ in range(n+1)]
    
    for u,v,l,t,idx in edges:
        # 교통량 0 가정 (l만 사용)
        if distStart[u] + l + distEnd[v] < minDist:
            answer.add(idx)
        if distStart[v] + l + distEnd[u] < minDist:
            answer.add(idx)

        # 최단경로 DAG 생성
        if distStart[u] + l + t + distEnd[v] == minDist:
            dag[u].append([v,idx])
            reverseDag[v].append([u,idx])
        if distStart[v] + l + t + distEnd[u] == minDist:
            dag[v].append([u,idx])
            reverseDag[u].append([v,idx])
            
            
    wayStart = [0] * (n+1)
    wayStart[1] = 1
    nodeSorted = sorted(range(1,n+1), key = lambda x: distStart[x])
    for u in nodeSorted:
        for v,idx in dag[u]:
            wayStart[v] += wayStart[u]
            
    wayEnd = [0] * (n+1)
    wayEnd[n] = 1
    nodeSortedReversed = sorted(range(1,n+1), key = lambda x: distEnd[x])
    for u in nodeSortedReversed:
        for v,idx in reverseDag[u]:
            wayEnd[v] += wayEnd[u]
            
    totalWay = wayStart[n]
    for u,v,l,t,idx in edges:
        w = l + t
        if distStart[u] + w + distEnd[v] == minDist:
            if wayStart[u] * wayEnd[v] == totalWay:
                answer.add(idx)
        elif distStart[v] + w + distEnd[u] == minDist:
            if wayStart[v] * wayEnd[u] == totalWay:
                answer.add(idx)
            
    answer = list(answer)
    answer.sort()
    
    if len(answer) == 0:
        answer = [-1]
        
    return answer