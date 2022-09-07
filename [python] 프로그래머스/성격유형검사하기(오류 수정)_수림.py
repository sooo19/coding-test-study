# 오류 점검 중
# 테스트 케이스 1 오답, 테스트 케이스 2 통과

def solution(survey, choices):
    answer = ''
    
    score = [[0]*2]*4       # R/T, C/F, J/M, A/N
    type = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]     # 유형 저장
    
    for i in range(len(survey)):
        if choices[i] >= 1 and choices[i] <= 3:
            per = survey[i][0]            
        else:
            per = survey[i][-1]
        
        addscore = 4 - choices[i] if choices[i] <= 4 else choices[i] - 4

        for i in range(4):
            for j in range(2):
                if per == type[i][j]:
                    print(per, type[i][j], addscore)
                    score[i][j] += addscore

        # 같은 열(0열 또는 1열)의 점수 값이 모두 + 되어 갱신됨
        # 예) score[0][0] 값이 + 되어야 하면, score[0][0], score[1][0], score[2][0], score[3][0] 값이 모두 증가함

    for i in range(4):
        if score[i][0] == score[i][1]:
            if ord(type[i][0]) < ord(type[i][1]):
                answer += type[i][0]
            else:
                answer += type[i][1]
        else:
            if score[i][0] > score[i][1]:
                answer += type[i][0]
            else:
                answer += type[i][1]
    
    print(score)

    return score

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])