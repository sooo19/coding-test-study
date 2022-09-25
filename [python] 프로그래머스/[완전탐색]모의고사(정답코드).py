# 다시 풀기
def solution(answers):
    answer = []
    
    total = []  # 모든 학생의 정답을 저장
    # 각 학생이 찍는 패턴을 기록
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    total.append(s1)
    total.append(s2)
    total.append(s3)
    
    count = [0]*len(total)      # 학생 인원 수 만큼 count 배열 생성
    for i in range(len(total)):     # s1, s2, s3의 정답을 모두 맞춰봄
        for j in range(len(answers)):    # 학생의 정답 패턴의 한 구간의 길이 재기
            k = j%len(total[i])     # 학생의 정답 패턴 길이로 해당 자리를 나눈 나머지
            if total[i][k] == answers[j]:    # 학생의 해당 번째 요소 정답과 answers의 해당 위치 값이 같으면 정답으로 인정
                count[i] += 1
    
    max_count = max(count)       # 정답을 가장 많이 맞춘 학생의 정답 개수를 구함
    for i in range(len(count)):
        if count[i] == max_count:
            answer.append(i+1)
    
    
    return answer