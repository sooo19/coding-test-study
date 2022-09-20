# 위에서 아래로 (문제)

# N 입력 받음
n = int(input())

# N개의 정렬할 숫자 입력 받아 배열에 저장
result = []
for i in range(n):
    x = int(input())
    result.append(x)

# 정렬 (내림차순)
result.sort(reverse=True)

# 출력
for j in result:
    print(j, end = ' ')
