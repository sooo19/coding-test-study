import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0     # 시작 지점의 최단경로는 0으로 초기화 (중요)

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        else:
            for i in graph[now]:  # i: (node, dist)
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
# print(distance)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])