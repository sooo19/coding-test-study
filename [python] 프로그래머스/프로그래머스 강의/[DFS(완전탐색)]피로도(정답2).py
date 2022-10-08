answer = 0
def DFS(k, cnt, dungeons, check):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if check[i] == 0 and k >= dungeons[i][0]:       # 방문하지 않은 던전이고, 현재 피로도가 해당 던전을 방문하기 위한 최소 피로도보다 크면
            check[i] = 1
            cnt += 1
            k -= dungeons[i][1]
            DFS(k, cnt, dungeons, check)
            k += dungeons[i][1]
            cnt -= 1
            check[i] = 0
    

def solution(k, dungeons):
    # answer = 0
    global answer
    check = [0]*len(dungeons)       # 방문 여부 체크하는 배열
    
    # cnt: 탐험한 던전 개수, k: 남은 피로도
    DFS(k, 0, dungeons, check)     # 0: 방문한 던전의 개수를 0으로 DFS 함수에 넘겨준다.
    
    return answer