def solution(routes):       # routes: 차량의 진입진출 정보
    answer = 0
    routes.sort(key = lambda x : x[1])      # 차량 정보를 진출 시점을 기준으로 정렬함
    
    point = routes[0][1]      # 첫 번째 차량의 진출지점을 포인트 지점으로 초기화
    answer = 1                # 카메라 한 대를 첫 번째 차량의 진출지점에 설치했으므로, 카메라 개수를 1개 추가함
    for i in range(1, len(routes)):
        if point < routes[i][0]:        # 현재 포인트 지점보다 새로운 차량의 진입지점이 더 크면 (겹치는 영역이 없으면) 포인트 지점을 바꿔주고, 카메라 한 대를 세움
            answer += 1                 # 카메라 개수 count
            point = routes[i][1]        # 포인트 지점 갱신
            
    return answer