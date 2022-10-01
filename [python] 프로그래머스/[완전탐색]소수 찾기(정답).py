# 소수 찾기 (정답)

from itertools import permutations
def solution(numbers):
    answer = 0
    
    perms = []
    for i in range(1, len(numbers)+1):
        for n in permutations(numbers, i):     # number 문자열의 각 자리 숫자들의 순열을 생성해 perms 배열에 삽입함
            p = ''.join(n)
            p = int(p)
            if p not in perms:
                perms.append(p)

        # perms = [''.join(n) for n in permutations(numbers)]
        # 위 for문을 위와 같이 한 줄로 작성 가능 
        # 단, 이 경우는 1부터 numbers 자릿수까지 순열에 사용하는 숫자의 개수를 변형하면서 순열을 생성한 코드는 아님
    
    for p in perms:
        div = 0     # 나머지가 0인 경우 (나눠 떨어지는 경우의 개수를 카운팅)
        for j in range(2, p):
            if p % j == 0:      # 나눠 떨어지면 (=> 여기서 나눠떨어지는 경우가 발생하면 바로 소수가 아닌 것으로 판별해야 연산량이 크게 줄어듦)
                # print(p, j)
                div += 1
                break
        if div == 0 and p != 0 and p != 1:       
            # 2부터 자기자신-1의 숫자까지 나눠떨어지는 숫자가 없으면 (=소수이면) 정답 변수를 1 증가시킴
            # 0과 1은 소수가 아니므로 p가 해당 숫자는 제외
            answer += 1
    return answer