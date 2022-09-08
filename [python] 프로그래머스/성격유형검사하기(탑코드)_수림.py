# https://velog.io/@phobos90/Programmers%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC%ED%95%98%EA%B8%B0-python
# 참고해서 최대한 깔끔한 코드 짜보기

# 프로그래머스 성격유형 검사하기 (Level 1)
def solution(survey, choices):
    answer = ''
    jipo = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}     # 지표 저장 (딕셔너리 활용)
    
    for i in range(len(survey)):
        left = survey[i][0]
        right = survey[i][1]
        
        if choices[i] - 4 < 0 :        # 왼쪽 지표 선택 (1<=점수<=3)
            jipo[left] += 4-choices[i]
        elif choices[i] - 4 > 0:        # 오른쪽 지표 선택 (5<=점수<=7)
            jipo[right] += choices[i]-4

    answer += "R" if jipo["R"] >= jipo["T"] else "T"
    answer += "C" if jipo["C"] >= jipo["F"] else "F"
    answer += "J" if jipo["J"] >= jipo["M"] else "M"
    answer += "A" if jipo["A"] >= jipo["N"] else "N"

    # 아래 if else문을 최대한 간단하게 나타낸 것이 위의 if else 문이다.

    # if jipo["R"] >= jipo["T"]:
    #     answer += "R"
    # else:
    #     answer += "T"
    
    # if jipo["C"] >= jipo["F"]:
    #     answer += "C"
    # else:
    #     answer += "F"

    # if jipo["J"] >= jipo["M"]:
    #     answer += "J"
    # else:
    #     answer += "M"

    # if jipo["A"] >= jipo["N"]:
    #     answer += "A"
    # else:
    #     answer += "N"

    return answer

# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))