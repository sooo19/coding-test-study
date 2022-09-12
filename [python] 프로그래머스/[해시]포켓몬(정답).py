# 시간 초과 문제 해결함
# 처음에는 순열(combination)을 통해 직접 뽑고, 뽑은 값의 중복을 제거해 개수를 세서 가장 개수가 많은 것을 출력함
# => 다른 방법을 찾아보면서 직접 뽑고 추릴 필요가 없음을 깨닫고 다른 방법으로 진행

def solution(nums):
    pick = len(nums)//2   # 뽑아야 하는 캐릭터의 개수
    count = len(set(nums))      # nums에 저장된 캐릭터 숫자의 중복을 제거한 후 개수 (중복을 제거한 캐릭터 개수)
    
    if pick < count:    # 뽑을 캐릭터 개수가 전체 캐릭터 개수(중복 x)보다 작은 경우
        answer = pick       # 뽑을 캐릭터 수가 정답이다
    else:
        answer = count  # 뽑을 캐릭터 개수가 전체 캐릭터 개수(중복 x)보다 큰 경우, 전체 캐릭터 개수가 정답
    
    return answer