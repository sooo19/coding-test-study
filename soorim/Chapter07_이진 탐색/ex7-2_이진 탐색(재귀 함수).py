# 재귀 함수로 구현한 이진 탐색

n, target = map(int, input().split())       # 원소 개수, 찾을 값 입력 받기
array = list(map(int, input().split()))     # 전체 원소 입력 받기

def binary_search(array, target, start, end):   # target: 찾으려고 하는 숫자
    if start > end:     # 끝까지 탐색했는데 값을 못 찾은 경우
        return None
    
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:   # mid를 기준으로 왼쪽에 target 값이 존재
        return binary_search(array, target, start, mid-1)
    else:   # mid를 기준으로 오른쪽에 target 값이 존재
        return binary_search(array, target, mid+1, end)


result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않음")
else:
    print(result+1)     # n번째에 타깃 값이 존재함