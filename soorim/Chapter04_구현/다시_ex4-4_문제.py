# 게임 개발
# 안됨

# 입력 예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# 왼쪽 방향으로 회전하며 (반시계 방향) 가보지 않은 육지를 찾음

n, m = map(int, input().split())
A, B, d = map(int, input().split())

map_array = []
for i in range(n):
    map_array.append(list(map(int, input().split())))

move_x = [-1, 0, 1, 0]      # 북, 동, 남, 서의 순서
move_y = [0, 1, 0, -1]

visited = [[0]*m for _ in range(n)]     # 방문 여부를 표시하는 배열
visited[A][B] = 1       # 시작 위치의 좌표를 방문한 좌표로 설정함

# 왼쪽으로 회전하는 함수
# def turn_left(direction):
#     direction -= 1      # 현재 방향에서 1 값을 빼주면 왼쪽으로 회전함
#     if direction == -1:
#         direction = 3    # 0에서 1을 빼면 -1인데, 이 때는 3일때의 방향과 같으므로 3을 return
#     return direction

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 게임 시뮬레이션 시작
count = 1   # 이동한 육지의 개수 세기
turn_time = 0   # 회전한 횟수
while True:
    # d = turn_left(d)        # 방향은 한 칸 정면으로 이동을 해도 계속 같은 방향임
    turn_left()
    # print('x, y좌표: ', A, B, ' => ')
    # print(visited)
    nx = A + move_x[d]
    ny = B + move_y[d]

    if visited[nx][ny] == 0 and map_array[nx][ny] == 0:  # 가지 않았던 곳인 경우 (정면)
        visited[nx][ny] = 1
        count += 1
        A, B = nx, ny
        # print("x, y좌표: ", A, B)
        # print('count : ', count)
        # print(visited)
        continue
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우 (회전해도 나아갈 곳이 없음)
    if turn_time == 4: 
        nx = A - move_x[d]  # 다시 뒤로 이동
        ny = B - move_y[d]
        if map_array[nx][ny] == 0:  # 뒤로 다시 이동한 칸이 육지이면
            A, B = nx, ny
        else:   # 뒤가 바다로 막혀 있는 경우
            break
        turn_time = 0   # turn_time은 0으로 초기화

print(count)
