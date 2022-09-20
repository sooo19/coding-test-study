# 음료수 얼려 먹기 (dfs 예제)

#  N(행) x M(열) 값과 음료수 배열 입력받음
n, m = map(int, input().split())

arr = []    # 음료수 배열 (visited 역할)
for i in range(n):
    arr.append(list(map(int, input())))
    # arr.append(list(input())) => 이렇게 넣으면 001, 010, 101 자체가 하나로 리스트에 저장됨

def dfs(i, j):
    # 영역이 좌표를 벗어나는지 확인
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if not arr[i][j]:
        arr[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):  # [0][0] -> [0][1] -> [0][2] -> ... -> [1][0] -> ... -> [n][0] -> ... [n][m] 순으로 탐색
       if not arr[i][j]:
            group = dfs(i, j)
            if group == True:
                count+=1

print(count)

# or 연산자 | 로 쓰지 않기 (중요!)