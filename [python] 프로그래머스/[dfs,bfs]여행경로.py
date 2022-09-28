def solution(tickets):
    # {"출발지: 도착지"} 딕셔너리 생성 => 딕셔너리 명: hash 
    hash = {}
    for i in range(len(tickets)):
        hash[tickets[i][0]] = 0
        
    for key in hash.keys():
        arr = []
        for i in range(len(tickets)):
            if key == tickets[i][0]:
                arr.append(tickets[i][1])
        arr.sort()
        hash[key] = arr
        
    # DFS
    stack = ["ICN"]     # 항상 "ICN" 공항에서 출발함
    path = []       # 최종 여행 경로 저장
    
    while stack:
        now = stack[-1]
        if now not in hash or len(hash[now]) == 0:
            path.append(stack.pop())    # 더 이상 갈 경로가 존재하지 않으면 해당 위치를 path 배열에 추가함
        else:
            stack.append(hash[now][0])      # 이동할 도시를 stack에 추가
            hash[now] = hash[now][1:]       # 방문한 도시를 빼고 저장
    
    answer = []
    for i in range(len(path)):      # path에는 여행지 이동 경로의 역순으로 저장되어 있으므로 path 배열의 역순을 answer 배열에 저장함
        answer.append(path[len(path)-i-1])
    # answer = path[::-1]       # 위 for문에서 실행한 배열 역순으로 저장과 동일한 코드
        
    return answer