from collections import deque
# cnt : 영역별 개수

def solution():
    answer = []
    N = int(input())

    # 그래프 입력 코드
    # graph = []
    # for i in range(N):
    #     graph.append(list(map(int, input())))

    # 더 깔끔한 그래프 입력 코드
    graph = [list(map(int, input())) for _ in range(N)]


    # 처음엔 아래처럼 코드를 작성해서
    # 그래프에 숫자가 int형이 아닌 str형으로 저장돼서 아예 0 또는 1로 인식이 안됨

    # for i in range(N):
    #     s = input()
    #     s_list = []
    #     for j in range(N):
    #         s_list.append(s[j])
    #     graph.append(s_list)
    

    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == 1:
                print(i, j)
                cnt = dfs(i, j, graph, visited, N)
                answer.append(cnt)

    print(len(answer))
    for i in range(len(answer)):
        print(i)

def dfs(x, y, graph, visited, N):
    cnt = 0     # 한 영역 당 개수

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
    
    return cnt


# print(solution())
solution()