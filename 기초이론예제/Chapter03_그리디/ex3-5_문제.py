# 1이 될때까지

# 입력 예시 (N, K)
# 25 5
# answer : 2

n, k = map(int, input().split())

# n=1이 될때까지 연산(빼기 또는 나누기) 진행
count = 0
while True:
    if n == 1:
        break
    if n % k != 0:
        n -= 1
        count+=1
    else:
        n /= k
        count+=1

print(count)
