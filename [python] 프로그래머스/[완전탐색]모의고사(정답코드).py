def solution(answers):
    # 어떤 학생이 가장 시험을 잘 봤는지 반환할 배열
    answer = []
    
    # 1~3번 학생들의 답안지
    student_answer = []
    student_answer.append([1,2,3,4,5])    # 1번 학생 정답
    student_answer.append([2,1,2,3,2,4,2,5])    # 2번 학생 정답
    student_answer.append([3,3,1,1,2,2,4,4,5,5])    # 3번 학생 정답
    
    count = [0,0,0]
    for i in range(len(student_answer)):
        for j in range(len(answers)):
            if student_answer[i][j%len(student_answer[i])] == answers[j]:
                count[i]+=1
    
    # count 배열에 각 학생의 맞은 개수가 작성됨
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)

    return answer