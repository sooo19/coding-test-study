# 퀵 정렬 (파이썬의 장점을 살린 코드)

# 내 코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:     # 리스트 원소가 하나이면 종료
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = []      # pivot 보다 작은 값
    right_side = []     # pivot 보다 큰 값
    for i in tail:
        if i > pivot:
            right_side.append(i)
        if i < pivot:
            left_side.append(i)
    
    # 배열의 합 이므로 (하나의 배열로 합침) pivot 값도 배열 형태로 넣어줘야 함
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


# 교재 코드 (동일한 의미)
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array):
#     if len(array) <= 1:     # 리스트 원소가 하나이면 종료
#         return array
    
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]     # pivot 보다 작은 값
#     right_side = [x for x in tail if x > pivot]     # pivot 보다 큰 값
    
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))
