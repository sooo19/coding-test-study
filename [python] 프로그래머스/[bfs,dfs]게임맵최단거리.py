from collections import deque
def solution(maps):
    answer = 0
    
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    answer = bfs(maps, visited, 0, 0)
    
    return answer

def bfs(maps, visited, x, y):
    n, m = len(maps), len(maps[0])
    
    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    