# 두 배열의 원소 교체
# 최대 K번 배열 A와 B의 값을 바꿔치기 해서 배열 A의 모든 원소의 합이 최대가 되도록 하는 문제

# 예시
# N = 5, K = 3
# array A = [1,2,5,4,3]
# array B = [5,5,6,6,5]

# N, K 값을 입력 받음
n, k = map(int, input().split())

# A, B 배열을 입력 받음
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

# A 배열은 오름차순, B 배열은 내림차순으로 정렬
arrayA.sort()
arrayB.sort(reverse=True)

# A 배열과 B 배열을 맨 앞의 값부터 차례로 교환
# 이 때 K번을 넘지 않으며, K번 교환하기 전에 A 배열 요소 값이 B 배열보다 커지면 교환 종료
for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break

result = sum(arrayA)

print(result)

# zip
# startwith
# string.startwith("")

# for pair zip()