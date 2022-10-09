from collections import deque
def solution(s, e):
    check = [0]*10001       # 1~10000까지의 좌표 번호 (방문 여부 체크 배열)
    queue = deque()
    queue.append(s)     # 현수의 처음 위치를 큐에 삽입
    check[s] = 1        # 처음 넣은 값도 방문여부 체크해줘야 함 (안해서 런타임에러 발생했었음)
    
    L = 0       # BFS의 현재 레벨 (정답을 담는 변수)
    while(queue):
        length = len(queue)
        for _ in range(length):
            now = queue.popleft()       # queue에 들어있는 숫자들을 하나씩 모두 pop하면서 이동 후의 좌표 값을 구함
            for nx in [now-1, now+1, now+5]:
                if nx == e:
                    return L+1      # 다음 노드가 e와 같으면, queue에 넣지 않고도 바로 Level에 1 추가한 값을 리턴 (넣고 빼서 발견하지 말기)
                # if check[nx] == 0 and nx > 0 and nx <= 10000:       # 방문하지 않았던 노드이고, 최대&최소 좌표범위 내에 들어오면
                if nx > 0 and nx <= 10000 and check[nx] == 0:
                    check[nx] = 1
                    queue.append(nx)        # 해당 노드로 이동
        L += 1      # 레벨 증가시킴 (다음 레벨로 넘어감)