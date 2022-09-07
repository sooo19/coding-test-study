# 부품 찾기
# 계수 정렬 활용 문제 풀이

n = int(input())

arrayN = [0]*1000001
for i in input().split():   # 입력 받은 매장 물품 번호에 해당하는 배열 요소의 값을 1로 변경 (있음을 표시)
    arrayN[int(i)] = 1

m = int(input())
arrayM = list(map(int, input().split()))

for i in arrayM:
    if arrayN[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
