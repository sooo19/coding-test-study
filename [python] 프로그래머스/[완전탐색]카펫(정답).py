# 정답

def solution(brown, yellow):
    answer = []
    
    y = []      # yellow의 인수분해 값을 저장
    for i in range(1, yellow+1):
        if yellow % i == 0 and yellow/i <= i:
            y.append([i, yellow/i])
    
    for i in range(1, brown+yellow+1):      # 전체 영역 (brown+yellow)의 인수분해 값 구하기 (전체를 구한 뒤 배열에 저장하는 형식이 아닌, 값을 하나씩 구하면서 조건에 만족하면 바로 정답으로 출력)
        if (brown+yellow) % i == 0 and (brown+yellow)/i <= i:
            if [i-2, (brown+yellow)/i-2] in y:
                answer = [i, (brown+yellow)/i]
                break       # 정답을 찾으면 바로 반복문 탈출 후 정답 리턴
    return answer

# 아이디어 (풀이)
# yellow 영역을 인수분해해서 n x m (n>=m)인 값을 모두 y 배열에 저장한다.
# 전체 영역 (brown + yellow)에 대해 인수분해를 진행하면서 전체 영역이 (n+2)x(m+2)로 이뤄지는 경우를 정답으로 리턴한다.