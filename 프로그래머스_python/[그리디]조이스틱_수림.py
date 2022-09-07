# 프로그래머스 그리디 문제
# 오답 (고쳐야 함)

def solution(name):
    answer = 0      # 조이스틱 움직임 횟수
    namelist = list(name)       # 이름을 알파벳 각 자리별로 잘라서 배열에 추가
                                # 알파벳 길이가 얼마인지 알 수 있음

    # 다음 알파벳 또는 이전 알파벳이 있음 (조이스틱 위, 아래)
    
    # 왼쪽, 오른쪽으로 모두 이동시켜서 각각 구해본 후 더 작은 값 return => 이 방법
    # _AA__ : 중간에 A가 뭉쳐있는 지점이 있으면 종료
    
    # for i in range(namelist()):
        
    # 0, 1, 2, 3, 4, 5 => len: 6
    # 오른쪽으로 가는 경우 : ___AA  이런 경우가 조기 종료되는 경우임
    right = 0
    for i in range(len(namelist)):
        if namelist[i] == 'A':      # 현재 값이 A
            for j in range(i, len(namelist)):
                Acount = 0
                if j == 'A':
                    Acount += 1
            if Acount != (len(namelist)-i):
            # 이어지는 남은 알파벳 중에 A가 아닌 것이 존재하는 경우, 넘어가는 횟수만 셈
                right += 1
            else:       # 남은 알파벳이 모두 A라면 (더이상 넘어가지 않고 종료)
                break
        else:   # 현재 값이 A가 아닌 경우
            right += min(ord(namelist[i]) - ord('A'), ord('Z')-ord(namelist[i]))
            right += 1
            # print('right: ', right)
        

    # 왼쪽으로 가는 경우 : _AA__ 이런 경우가 조기 종료되는 경우임
    # 시작은 무조건 0번째 배열 값
    left = 0
    # 첫째 자리 조작 여부 판단
    if namelist[0] == 'A':
        left += 0
    else:
        left += min(ord(namelist[0]) - ord('A'), ord('Z')-ord(namelist[0]))

        # 왼쪽으로 커서 이동 
        for j in range(len(namelist)-1, 0, -1):     # _AAAAA 경우인지 확인
            Acount = 0
            if namelist[j] == 'A':
                Acount += 1

            if Acount == j:     # _AAAAA 이면 종료
                break
            else:       # 커서를 움직여야 하는 경우  _AA___
                left += 1
                if namelist[j] == 'A':
                    left += 0
                else:
                    left += min(ord(namelist[j]) - ord('A'), ord('Z') - ord(namelist[j]))
    
    
    answer = min(right, left)
            
    
    # print(ord('J')-ord('A'))      결과 : 9
    # print(namelist)
    
    
    return answer

print(solution('JEROEN'))

# AAA
# JAZ

# 테스트 케이스
# JAN : 오른쪽으로 이동하면서 해결
# JEROEN : 왼쪽으로 이동하면서 해결