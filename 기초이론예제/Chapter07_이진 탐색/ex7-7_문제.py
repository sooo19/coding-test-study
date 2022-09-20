# 부품 찾기
# 집합 자료형 사용

n = int(input())
arrayN = set(map(int, input().split()))     # 가게에 있는 부품 번호를 입력받아 집합(set) 자료형에 기록

m = int(input())
arrayM = list(map(int, input().split()))

for i in arrayM:
    if i in arrayN:     # 집합 내의 모든 원소 중 i 값이 있는지 확인 가능
        print('yes', end=' ')
    else:
        print('no', end=' ')