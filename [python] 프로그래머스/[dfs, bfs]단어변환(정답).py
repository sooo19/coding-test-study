# 정답

from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0 for i in range(len(words))]       # 단어의 개수만큼 visited 배열 생성
    
    queue = deque()
    queue.append([begin, 0])    # 시작 단어, 단어변환 횟수를 큐에 삽입

    while queue:
        nword, ncnt = queue.popleft()
        
        if nword == target:     # 현재 단어가 target 단어와 같다면 현재까지의 변환 횟수를 리턴
            answer = ncnt
            break
        else:   # 다르면, 한 글자만 다른 단어를 찾아야 함
            for i in range(len(words)):     # words 배열의 모든 단어들의 visited를 탐색
                if visited[i] == 0:     # 방문하지 않은 노드이면 해당 단어가 현재 단어와 몇 글자가 다른지 파악
                    tmp_cnt = 0
                    for j in range(len(nword)):
                        if nword[j] != words[i][j]:
                            tmp_cnt += 1    # 글자가 다른 자리마다 temp count 값을 1씩 추가
                    if tmp_cnt == 1:    # 한 글자 다른 단어이면
                        ncnt += 1   # 변환 횟수를 증가시킴
                        queue.append([words[i], ncnt])   # 바꿀 단어를 큐에 삽입
                        visited[i] = 1      # 방문 여부를 참으로 바꿈

    return answer
