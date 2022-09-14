def solution(clothes):
    answer = 1
    
    hash = {}
    for i in range(len(clothes)):
        hash[clothes[i][-1]] = 0
    
    for i in range(len(clothes)):
        if clothes[i][-1] in hash:
            hash[clothes[i][-1]] += 1
    
    for i in hash:
        answer *= hash[i]+1    # 옷을 선택하지 않는 경우도 추가해서 곱하기 (각 경우는 '한 종류 옷의 가지 수 + 1')
    answer -= 1     # 아무것도 선택하지 않는 경우 한 가지는 빼기
    
    return answer