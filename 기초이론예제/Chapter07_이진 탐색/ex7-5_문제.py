# 부품 찾기
# 이진 탐색 알고리즘 활용 풀이

# 매장 제품 수, 제품 종류(n, arrayN)와 사용자 입력 제품 수, 제품 종류 (m, arrayM)를 입력 받음
n = int(input())
arrayN = list(map(int, input().split()))

m = int(input())
arrayM = list(map(int, input().split()))

# 매장의 제품을 정렬 => 매장 제품 정렬 후 이진 탐색으로 사용자가 입력한 제품을 탐색함
arrayN.sort()

# 반복문(while문)을 사용한 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid+1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

# 결과 출력
for i in arrayM:
    result = binary_search(arrayN, i, 0, n-1)
    if result == None:  # 찾은 결과가 없으면 no 출력
        print('no', end = ' ')
    else:               # 찾은 결과가 있으면 yes 출력
        print('yes', end = ' ')