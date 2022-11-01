import heapq
INF = int(1e9)

def solution(n, edge):
    answer = 0
    
    distance = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))
    
    queue = []
    start = 1
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        else:
            for i in graph[now]:        # i : (node, cost)
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
    
    distance[0] = 0
    max_length = max(distance)
    
    for d in distance:
        if max_length == d:
            answer += 1
    
    return answer