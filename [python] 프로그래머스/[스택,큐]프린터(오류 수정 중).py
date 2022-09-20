# 오류 수정 중
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    
    wonder = priorities[location]     # 사용자가 출력 순서를 궁금해하는 출력물 값
    
    print_val = []      # 인쇄 순서 저장 배열
    # priorities 배열에서 위치한 배열 번호+1 값이 각 요소의 고유 번호로 지정함
    # 최종 인쇄할 순서를 저장하는데, 이 때 각 출력물의 고유 번호를 배열의 요소로 저장함
    count = 0
    start = 0   # 동일한 우선순위의 출력물이 있는 경우, 출력의 기준이 되는 시점

    for i in range(len(priorities)):
        max_val = max(priorities)
        
        if max_val == 0:
            break
        
        if priorities[i] == max_val:
            count += 1
        
        if count == 1:
            print_val.append(i+1)
            priorities[i] = 0
        else:
            # 최댓 값이 2개 이상인 경우, 앞선 최댓값의 바로 다음 값부터 배열 끝까지, 처음부터 최댓값의 앞 값까지 순서로 print_val 배열에 넣으려고 함 (근데 안됨)
            for j in range(start, len(priorities)):
                if max_val == priorities[j]:
                    print_val.append(j+1)
                    priorities[j] = 0
            for j in range(0, start):
                if max_val == priorities[j]:
                    print_val.append(j+1)
                    priorities[j] = 0
    
    for i in range(len(print_val)):
        if print_val[i] == wonder:
            answer = i + 1
            
    return answer