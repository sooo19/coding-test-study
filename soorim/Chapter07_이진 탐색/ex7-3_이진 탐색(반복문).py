# 반복문(while문)으로 구현한 이진 탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # 타깃이 중앙 값보다 왼쪽에 존재 (타깃이 중앙 값보다 작음)
            end = mid-1
        else:       # 타깃이 중앙 값보다 오른쪽에 존재 (타깃이 중앙 값보다 큼)
            start = mid+1

# n(숫자 개수), target 값 입력 받음
n, target = map(int, input().split())
array = list(map(int, input().split()))     # 배열 입력 받음

result = binary_search(array, target, 0, n-1)

# 결과 출력
if result == None:
    print('원소가 존재하지 않음')
else:
    print(result+1)