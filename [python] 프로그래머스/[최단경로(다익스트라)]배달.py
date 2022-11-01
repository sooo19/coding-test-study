import heapq
INF = int(1e9)
# N: 노드 개수
# K: 배달 가능한 최대 거리
# 시작 지점: 1번 마을

def solution(N, road, K):
    answer = 0      # 자기 자신은 포함
    
    distance = [INF]*(N+1)      # 최단경로 기록
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    
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
    
    for i in distance:
        if i <= K:
            answer += 1

    return answer