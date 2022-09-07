# BFS 예제
# queue 사용
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True   # 방문한 노드를 확인
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:  # start(=1)과 연결된 노드들부터 탐색 => 처음에는 [2, 3, 8]
            if not visited[i]:  # if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

bfs(graph, 1, visited)