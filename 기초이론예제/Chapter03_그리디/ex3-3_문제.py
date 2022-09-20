# 숫자 카드 게임
# 특정 행을 선택하고 그 행에서 가장 작은 숫자를 뽑을 때, 이렇게 뽑는 방법 중 가장 큰 숫자를 뽑도록 함

# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# answer : 2

n, m = map(int, input().split())
arr = []
min_arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    min_arr.append(min(arr[i]))

answer = max(min_arr)

print(answer)
