# 시간 초과

from itertools import combinations

# 1) 리스트 중복 요소 제거 : for문(반복문) 사용하기
def solution(nums):
    comb = list(combinations(nums, len(nums)//2))
    
    lens = []
    for arr in comb:
        alist = []
        for i in range(len(arr)):
            if arr[i] not in alist:
                alist.append(arr[i])
        lens.append(len(alist))
    
    answer = max(lens)
        
    return answer

# 2) 리스트 중복 요소 제거 : set 연산 사용하기

from itertools import combinations

def solution(nums):
    comb = list(combinations(nums, len(nums)//2))
    
    lens = []
    for arr in comb:
        alist = list(set(arr))
        lens.append(len(alist))
    
    answer = max(lens)
        
    return answer