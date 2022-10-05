import collections          # 딕셔너리 사용을 위한 라이브러리
def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))      # report 배열의 중복 요소 제거
    
    # 해시 자료구조 2개 생성
    reportHash = collections.defaultdict(set)       # 신고자와 신고받은 사람
    stoped = collections.defaultdict(int)           # 한 사람 당 신고받은 횟수
    
    for x in report:
        a, b = x.split(" ")
        reportHash[a].add(b)        # add 문법 (딕셔너리의 set 형식인 value에 값을 추가할 때는 add 함수를 사용함)
        stoped[b] += 1
    
    for id in id_list:
        mail = 0        # 한 사람당 신고한 사람 중 계정 정지된 아이디의 수를 카운팅
        for user in reportHash[id]:
            if stoped[user] >= k:
                mail += 1
        answer.append(mail)
    
    return answer