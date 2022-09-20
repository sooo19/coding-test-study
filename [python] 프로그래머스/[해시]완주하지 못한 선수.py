def solution(participant, completion):
    answer = ''
    
    p = list(set(participant))      # 참가자 배열을 set 연산하여 배열 p에 저장 (동명 이인이 있을 수 있으므로 set 연산을 통해 중복되지 않은 이름만 저장)
    
    hash = {}
    for i in p:     # hash를 만들어서 {"참가자 이름" : 0} 형태로 저장
        hash[i] = 0
    
    for i in participant:   # 참가자의 수만큼 hash 값을 갱신(1씩 추가, 동명이인인 경우 해시 값이 2 이상으로 표기됨)
        hash[i] += 1
    
    for i in completion:    # 완주한 참가자들의 해시 값을 1씩 감소시킴
        hash[i] -= 1
    
    for i in hash:      # 최종적으로 해시 값이 1인 참가자를 return (완주 못한 참가자임)
        if hash[i] == 1:
            return i