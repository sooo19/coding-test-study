# 상하좌우 (여행가 움직임 문제)
# ** 일반적인 좌표 평면 생각하지 말고, 문제에 나오는 좌표평면 생각하기

# 입력 예시
# 5 => N
# R R R U D D
# answer : 3 4

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()     # L R U D 문자열 입력받기 (한 변수에 문자열을 입력받을 수 있음)

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# (0, -1): D, (0, 1): U, (-1, 0): L, (1, 0): R
move_types = ['L', 'R', 'U', 'D']

for p in plans:
    for i in range(len(move_types)):
        if p == move_types[i]:
            if (x + dx[i] > 0) & (y + dy[i] > 0) & (x + dx[i] <= n) & (y + dy[i] <= n):
                # 좌표 값은 1 이상, n 이하
                x += dx[i]
                y += dy[i]

print(x, y)
        