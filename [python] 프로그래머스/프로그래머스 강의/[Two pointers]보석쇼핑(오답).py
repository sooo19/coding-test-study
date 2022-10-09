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