from collections import deque

def BFS():
    queue = deque()
    queue.append(1)
    L = 0
    while(queue):
        length = len(queue)     # length : 해당 Level에서의 원소의 개수
        for _ in range(length):     # level의 개수만큼 큐에 append&popleft 진행함
            v = queue.popleft()
            print(v, end = ' ')
            for nv in [v*2, v*2+1]:     # 해당 노드의 아래 가지 2개
                if nv > 7:
                    continue    # nv가 7보다 크면 append되지 않음
                queue.append(nv)
        L += 1      # Level 증가 (아래로 내려감)

BFS()