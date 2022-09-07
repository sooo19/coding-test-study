# 특정 거리의 도시 찾기
# BFS : 모든 간선의 비용이 동일할 때 (가중치가 1로 같음) BFS 사용함
# 최단 경로 문제에서는 BFS 사용 (p.152, p.339)

# 입력 예시
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]     # 1~4를 인덱스로 가지는 2차원 배열 생성 => 해당 인덱스 번호의 요소를 연결된 칸으로 저장
# 저장된 예시
# graph = [[], [2, 3], [3, 4], [], []]

# 모든 도로 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)      # a -> b로 연결되어 있는 관계를 graph[a]에 b 값을 저장하는 것으로 표현

# 모든 도시에 대한 최단 거리를 -1로 최소화 (방문 여부를 판별하는 배열)
distance = [-1]*(n+1)
distance[x] = 0     # 출발 지점의 최단거리는 0으로 설정 (x -> x 는 거리가 0)

# BFS 수행
queue = deque([x])
while queue:
    now = queue.popleft()       # 출발 지점 값을 빼냄 (= 현재 위치)
    for next in graph[now]:     # 현재 노드와 연결된 노드들을 모두 탐색
        if distance[next] == -1:    # 아직 방문하지 않은 노드라면
            queue.append(next)
            distance[next] = distance[now] + 1  # 이동 거리 1 추가

check = 0   # 최단거리가 k인 노드가 있는지 없는지 여부 판단
for i in range(1, n+1):
    if distance[i] == k:
        print(i, end=' ')
        check += 1

if check == 0:
    print(-1)



# print(graph)