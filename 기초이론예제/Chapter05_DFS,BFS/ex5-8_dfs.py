# DFS 예제

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')   # 방문 순서대로 출력

    for i in graph[v]:
        if not visited[i]: # if visited[i]==False:
            dfs(graph, i, visited)

# 2차원 리스트로 각 노드의 연결 정보 표현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드에 대한 방문 정보 표현
visited = [False] * 9

dfs(graph, 1, visited)  # 1번 노드부터 방문 시작