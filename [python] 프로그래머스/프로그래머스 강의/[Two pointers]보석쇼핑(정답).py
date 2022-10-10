# 정답 코드 구현

import collections
def solution(gems):
    answer = []
    hash = collections.defaultdict(int)
    length = len(set(gems))     # 중복되지 않는 보석의 종류 개수
    left = 0        # left pointer의 첫 시작점
    max_length = 100000     # 최대 길이는 보석의 개수로 설정
    
    for right in range(len(gems)):
        hash[gems[right]] += 1      # 보석(키 값)에 대한 개수(value)를 증가시킴
        while(len(hash) == length):     # hash 길이가 (=key값의 개수가) length개 일때만 실행
            if right-left+1 < max_length:       # max_length 갱신이 가능한 경우, 새로운 값으로 바꿔줌
                max_length = right-left+1       # 최대 길이와 이때의 구간 저장
                answer = [left+1, right+1]
                
            hash[gems[left]] -= 1           # left를 오른쪽으로 한칸씩 옮기면서 이동이 가능한지 파악
            if hash[gems[left]] == 0:       # 해당 키 값의 value가 0이면, 해당 키를 삭제
                del hash[gems[left]]
            left += 1                       # 키가 삭제되지 않았다면, left를 오른쪽으로 이동시킴
    return answer


# ========================================================================
# # 2번째로 생각한 아이디어로 구현한 코드 (딕셔너리 사용)

# import collections
# def solution(gems):
#     answer = []
    
#     dict = {}
#     for i in range(len(gems)):
#         dict[gems[i]] = []
    
#     for i in range(len(gems)):
#         dict[gems[i]].append(i+1)
#     print(dict)

#     for i in dict.keys():
#         answer.append(dict[i][0])
    
#     answer = [min(answer), max(answer)]
#     return answer