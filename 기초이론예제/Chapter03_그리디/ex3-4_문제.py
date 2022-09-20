# 숫자 카드 게임 (2중 반복문 구조 사용)

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_val = 10001     # 최대 입력 가능 값인 10000보다 1 큰 수

    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

    # print('min value: ', min_value)

print(result)