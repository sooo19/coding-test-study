from collections import deque
cnt = 0

def solution():
    global cnt
    answer = []
    N = int(input())

    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == 1:
                dfs(i, j, graph, visited, N)
                answer.append(cnt)

    print(len(answer))
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])


def dfs(x, y, graph, visited, N):
    global cnt
    cnt = 0     # 한 영역 당 단지 개수

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1       # visited 1이면 다시 방문하지 않음
    cnt += 1

    dx = [0, 0, -1, 1]      # 상하좌우
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

solution()