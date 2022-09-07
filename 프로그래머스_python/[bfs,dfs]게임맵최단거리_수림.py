# BFS/DFS 문제
# (1,1)에서 게임 캐릭터가 시작해서 (n,m)까지 최단거리로 가는 문제 (최단 거리 값 구하기) 

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
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    

    
