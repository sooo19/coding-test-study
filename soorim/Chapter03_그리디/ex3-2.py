# 큰 수의 법칙 (그냥 더하는 방법)
# 입력 예시
# 5 8 3 (N, M, K)
# 2 4 5 4 6

# N, M, K 값을 공백으로 입력받기
n, m, k = map(int, input().split()) # 입력 받은 세 개의 숫자를 공백을 기준으로 나눔, 모두 정수형으로 변환

# N개의 숫자를 공백으로 구분해 입력받기 (배열로 저장)
data = list(map(int, input().split()))

# 내림차순으로 정렬 => 6, 5, 4, 4, 2
data.sort(reverse = True)

# 정렬한 배열의 0, 1번째 요소를 가지고 덧셈 연산 진행 => 6+6+6+5+6+6+6+5 = 46
answer = 0

while True:
    for i in range(k):  # 가장 큰 수를 세 번(k번) 더하기
        if m == 0:  # m이 0이면 (더해야 하는 횟수를 모두 더하면) 탈출
            break
        answer += data[0]   # 가장 큰 값을 더함
        m -= 1  # 한 번 더할 때마다 m 값 줄여주기
    if m == 0:  
        break
    else:
        answer += data[1]   # 두 번째로 큰 값을 더햄
        m -= 1

print(answer)


