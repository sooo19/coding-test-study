import math
def solution(fees, records):
    answer = []
    
    # 세 가지의 배열을 선언
    inTime = [0]*10000      # 들어온 시간
    isIn = [0]*10000        # 차량이 있는지 여부
    sumTime = [0]*10000     # 머무른 시간 저장
    
    for record in records:
        a, b, c = record.split(" ")     # a: 시각, b: 차량번호, c: IN/OUT
        h, m = a.split(":")     # 시간, 분을 저장
        
        if c == 'IN':
            inTime[int(b)] = 60*int(h)+int(m)
            isIn[int(b)] = 1
        else:       # c == 'OUT'
            sumTime[int(b)] += (int(h)*60+int(m)) - inTime[int(b)]
            isIn[int(b)] = 0
    
    for i in range(10000):      # 나가지 않은 차량에 대한 계산 실행
        if isIn[i] == 1:
            sumTime[i] += (23*60+59) - inTime[i]
            
    for x in range(10000):
        if sumTime[x] > 0:
            answer.append(fees[1]+max(math.ceil((sumTime[x]-fees[0])/fees[2]), 0)*fees[3])
            
            # 아래 코드를 위 코드 한 줄로 간략히 작성함
            # plusmoney = max(math.ceil((sumTime[x]-fees[0])/fees[2]), 0)*fees[3]
            # fee = fees[1]+plusmoney
            # answer.append(fee)
            
        
    return answer


# math.ceil() : 반올림 함수  => 사용을 위해 math 라이브러리를 import 함
# fees[0] : 기본 시간 (요금이 부과되지 않는 기본 시간)
# fees[1] : 기본 요금
# fees[2] : 단위 시간 (몇 분 단위로 추가 요금을 부과할 것인지)
# fees[3] : 단위 요금 (얼마 요금을 추가로 부과할 것인지)