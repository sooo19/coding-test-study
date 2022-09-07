# 미로 찾기
# 중간 중간 값 출력해보면서 제대로 실행되는지 확인

# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)

from collections import deque

# n, m, 그래프 입력 받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향
dx = [-1, 1, 0, 0]  # 위, 아래, 왼, 오
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐
    queue = deque()
    queue.append((x, y))  # 제일 처음 : (0,0)이 저장됨

    while queue:    # queue 안에 값이 차있는 동안 반복 (큐가 빌때까지 while문 반복)
        # 상하좌우 갈 곳 탐색 (가장 최근 노드를 뺌)
        x, y = queue.popleft()
        print('x, y: ', x, y)
        for i in range(4):
            nx = x + dx[i]  # 이동한 새로운 x, y좌표 계산
            ny = y + dy[i]
            print('nx, ny: ', nx, ny)

            if nx >= 0 and nx < n and ny >=0 and ny < m:
                if graph[nx][ny] == 1:  # 방문하지 않은 노드인지 확인
                    graph[nx][ny] = graph[x][y] + 1
                    print('queue에 append 되는지 확인')

                    queue.append((nx, ny))
                    print(x, y, ' => ', nx, ny, ', 방문 횟수: ', graph[nx][ny])
                    print('queue에 남은 값: ', queue)
    return graph[n-1][m-1]      # 도착 지점의 그래프 값(노드를 방문한 횟수를 기록한 값) 출력

# 결과 출력
result = bfs(0, 0)
print(result)
