import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)      # 무한을 의미하는 값으로 10억을 설정

# 1) 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 2) 시작 노드 번호 입력받기
start = int(input())

# 3) 각 노드에 연결된 노드 정보를 담는 리스트
graph = [[] for _ in range(n+1)]

# 4) 최단거리 테이블을 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # c : a번 노드 -> b번 노드로 가는 비용
    graph[a].append((b, c))       # 양방향인 경우 모두 추가해주기 -> graph[b].append(a, c)

def dijkstra(start):
    queue = []
    # 시작노드(자기 자신)로 가는 비용인 0을 큐에 삽입
    heapq.heappush(queue, (0, start))       # 비용(0), 노드(시작)
    distance[start] = 0

    while queue:        # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(queue)         # 비용, 노드번호를 현재 값으로 갱신
        # 현재 노드가 이미 처리된 적이 있다면 무시 (최단거리 테이블에 저장된 값이 더 작다면 continue)
        if distance[now] < dist:        # 현재 노드의 최단거리 테이블 값 < 현재 노드의 비용
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:        # i는 (node, dist) 꼴
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[i[0]] > cost:       # 새로 계산한 cost 비용이 더 작으면
                distance[i[0]] = cost       # 최단거리 값을 갱신
                heapq.heappush(queue, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력 (start 노드에서 각 노드들로 가기 위한 최소비용)
for i in range(1, n+1):
    # 도달할 수 없는 경우, 값으로 무한을 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우, 최단거리를 출력
    else:
        print(distance[i])














