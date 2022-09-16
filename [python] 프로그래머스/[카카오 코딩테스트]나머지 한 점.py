# 코테 데모 문제 (환경 테스트)로 나옴
# https://school.programmers.co.kr/learn/courses/18/lessons/1878

def solution(v):
    hash = {}		# x, y좌표 언급 횟수 카운팅
    for i in range(len(v)):
        hash[v[i][0]] = [0, 0]
        hash[v[i][1]] = [0, 0]
        
    x, y = 0, 0
    for i in range(len(v)):		# 좌표 값을 딕셔너리의 key로, 언급된 횟수를 value 값으로 저장
        hash[v[i][0]][0] += 1 
        hash[v[i][1]][1] += 1 
    
    for i in hash.keys():		# 해시의 key 값을 불러오는 방법 
        if hash[i][0] == 1:		# 언급 횟수가 1번이면 x좌표로 지정
            x = i
        if hash[i][1] == 1:		# 언급 횟수가 1번이면 y좌표로 지정
            y = i
    
    answer = [x, y]
    
    return answer