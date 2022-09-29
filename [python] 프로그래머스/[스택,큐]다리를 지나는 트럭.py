# 다리를 지나는 트럭
# bridge_length는 다리의 길이, weight는 다리에 최대로 지나갈 수 있는 트럭 무게, truck_weights는 각 트럭의 무게 정보를 담은 배열이다
# 길이 1만큼의 다리를 지나는데 시간 1이 소요될 때, 최종적으로 모든 트럭이 다리를 지난 후 걸리는 시간을 구해라.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0]*bridge_length     # 다리 위에 놓인 트럭 정보
    
    while queue:
        answer += 1
        queue.pop(0)      # 큐의 맨 앞의 값(도착지점에 도착한 트럭 자리)을 빼준다
        if len(truck_weights) > 0: 
            if sum(queue) + truck_weights[0] <= weight:   # 새로운 트럭이 들어와도 다리 위 최대 무게를 초과하지 않으면
                plus = truck_weights.pop(0)     # 추가할 트럭의 무게
                queue.append(plus)       # 다리 위에 해당 트럭의 무게를 추가함
            else:
                queue.append(0)      # 추가할 수 없는 경우 0을 추가함(다음 트럭을 다리 위에 올리지 않음)
    
    return answer