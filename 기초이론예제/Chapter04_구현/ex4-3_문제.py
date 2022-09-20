# 왕실의 나이트

# 이동 가능한 경우의 수
# 왼 2 위 1 : (-2, -1)
# 왼 2 아래 1 : (-2, 1)
# 오 2 위 1 : (2, -1)
# 오 2 아래 1 : (2, 1)
# 위 2 왼 1 : (-1, -2)
# 위 2 오 1 : (1, -2)
# 아래 2 왼 1 : (-1, 2)
# 아래 2 오 1 : (1, 2)

# 현위치
location = input()
# x, y = map(int, location.split())     split()은 공백을 기준으로 띄어쓰기 됨
x = int(ord(location[0]))    # 문자
y = int(location[1])         # 숫자

# 갈 수 있는 경우의 수
steps = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

count = 0   # 갈 수 있는 위치를 세는 변수
for i in range(len(steps)):
    nx, ny = 0, 0
    nx = x + steps[i][0]    # new x
    ny = y + steps[i][1]    # new y

    if (nx >= ord('a')) & (nx <= ord('h')) & (ny >= 1) & (ny <= 8):
        count += 1

print(count)
