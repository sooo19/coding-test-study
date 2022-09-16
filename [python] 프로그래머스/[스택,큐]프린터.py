# 프린터 (스택, 큐)

def solution(priorities, location):
    answer = 0
    # priorities 배열 안의 최댓값을 계속 갱신해가면서 location 요소와 동일한 값을 찾을 때까지 반복
    while True:
        max_num = max(priorities)
        for i in range(len(priorities)):
            if max_num == priorities[i]:    # 최댓 값과 리스트의 요소가 일치하면
                answer += 1     # 프린트 진행, 프린트한 순번을 저장
                # 우선순위가 큰 값부터 프린트하므로 프린트 순번은 1씩 증가시키면 됨
                priorities[i] = 0       # 출력한 값은 우선순위를 0으로 갱신
                max_num = max(priorities)       # 배열의 새로운 최댓값 갱신
                if i == location:   # i값이 찾는 값인 location과 같다면 정답 리턴
                    return answer

    return