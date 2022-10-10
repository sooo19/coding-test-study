# 2번째로 생각한 아이디어로 구현한 코드 (딕셔너리 사용)

import collections
def solution(gems):
    answer = []
    
    dict = {}
    for i in range(len(gems)):
        dict[gems[i]] = []
    
    for i in range(len(gems)):
        dict[gems[i]].append(i+1)
    print(dict)

    for i in dict.keys():
        answer.append(dict[i][0])
    
    answer = [min(answer), max(answer)]
    return answer