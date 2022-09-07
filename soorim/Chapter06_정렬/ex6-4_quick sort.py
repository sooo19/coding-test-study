# 퀵 정렬
# 원리
# : pivot 설정 후, 피벗을 기준으로 왼쪽(작은 숫자), 오른쪽(큰 숫자) 나눔 => 분할(=파티션)
# : 나눈 영역에 대해 다시 pivot 설정 후 분할하는 과정을 반복
# => 재귀 함수 형태로 코드 작성하는 것이 효율적

# 퀵 정렬의 종료 조건 : 원소의 개수가 1개인 경우 모두 배열되었다고 판단해 종료함

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소의 개수가 1개인 경우 종료
        return
    pivot = start       # 첫 번째 원소를 pivot으로 설정
    left = start+1      # 피벗에서 왼->오 방향으로 피벗보다 큰 값 찾기
    right = end         # 피벗에서부터 가장 떨어진 끝 값에서 오->왼 방향으로 피벗보다 작은 값 찾기

    while left <= right:
        # 큰 값, 작은 값 찾는 영역이 교차되면 (왼쪽에 작은 값, 오른쪽에 큰 값이 나오면) 종료 (피벗을 찾은 작은 값으로 갱신)
        while left <= end and array[left] <= array[pivot]:      # 피벗보다 큰 값 찾기 (left는 end(끝점)값을 초과할 수 없음)
            left+=1
        while right > start and array[right] >= array[pivot]:   # 피벗보다 작은 값 찾기 (right는 start(시작점)값 보다 작을 수 없음)
            right-=1
        
        # left 값과 right 값을 찾음
        if left > right:    # 피벗 교체 (left와 right가 교차함)
            array[pivot], array[right] = array[right], array[pivot]
        else:   # left 값과 right 값을 서로 교체 (left와 right가 교차하지 않음)
            array[left], array[right] = array[right], array[left]
        
        # 분할 이후 오른쪽, 왼쪽에서 각각 정렬 수행
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)