# 큰 수의 법칙 (수열 계산으로 더하는 방법)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]     # 배열에서 가장 큰 수
second = data[1]    # 배열에서 두 번째로 큰 수

# 5 8 3
# 2 4 5 4 6
# => 6 6 6 5 + 6 6 6 5

# 완벽한 수열 개수
num1 = m // (k+1)
# print(num)

# 완벽하지 못한 수열의 숫자 개수
num2 = m % (k+1)

# print(num1, num2)
answer = num1*(first*k+second) + num2*first
print(answer)