# cnt 변수를 전역변수로 선언하지 않고 DFS에서 최종 cnt를 solution 함수로 리턴받아 사용함
# 이때 제대로 된 정답이 출력되지 않는데, 그 이유 찾아내보기

def DFS(v1, cnt, check, graph):
    check[v1] = 1       # 현재 노드를 방문했다고 체크
    cnt += 1
    for i in graph[v1]:
        if check[i] == 0:       # 연결된 노드들 중 방문하지 않은 노드들을 계속 탐색
            DFS(i, cnt, check, graph)
    return cnt
            

def solution(n, wires):
    answer = 100    # 최솟값을 찾는 것이므로, 최대 값을 초기 answer의 값으로 초기화함
    
    graph = [[] for _ in range(n+1)]        # 연결된 간선 정보를 저장할 그래프 생성 (1~9번 배열에 각각 연결된 노드 정보를 저장할 것임)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)        # 만약 그래프가 단방향 그래프이면, 이 줄의 코드는 생략
        
    for v1, v2 in wires:        # 연결된 간선들을 차례로 하나씩 끊어가면서 양쪽 노드의 개수 차를 비교함
        check = [0]*(n+1)
        check[v2] = 1       # 끊을 노드의 (a, b) 중 b 노드의 check 여부를 참으로 바꿈 (이미 방문한 노드라 가정하고 다시 못하도록 함)
        cnt = 0         # 한 영역에 연결된 노드의 개수
        cnt_v1 = DFS(v1, cnt, check, graph)       # 끊을 노드 (a,b)의 a 값과 방문여부 체크 배열, 그래프 배열을 DFS에 넘겨줌
        # 한 쪽의 송전탑의 개수 : cnt개, 다른 쪽의 송전탑의 개수 : n-cnt
        # answer : 현재까지 양 쪽 송전탑 개수 차의 최솟값
        answer = min(answer, abs(cnt_v1-(n-cnt_v1)))
        
    return answer