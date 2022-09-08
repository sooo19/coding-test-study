# 프로그래머스 신고 결과 받기 (Level1 문제)
# 시간 초과 에러 나타남 (실패!)

def solution(id_list, report, k):
    answer = []     # 신고한 회원 중 정지당한 회원 수 기록
    
    count = {}      # 신고 횟수 count
    for i in range(len(id_list)):
        count[id_list[i]] = 0
    
    report2 = []
    for i in report:
        if i not in report2:
            report2.append(i)
        
    report = []
    for i in report2:
        report.append(i.split(" "))
    
    for i in range(len(report)):     # 신고한 사람:i[0], 신고받은 사람:i[1]
        count[report[i][-1]] += 1

    singo = []
    for i in id_list:
        if count[i] >= k:
            singo.append(i)     # 신고 당한 사람 추림
            
    answer2 = {}    # 회원: 신고해서 정지된 회원 수 (딕셔너리 생성)
    for i in range(len(id_list)):
        answer2[id_list[i]] = 0

    for i in range(len(report)):
        if report[i][-1] in singo:
            answer2[report[i][0]] += 1
    
    for i in id_list:
        answer.append(answer2[i])

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

ans = solution(id_list, report, k)
print(ans)