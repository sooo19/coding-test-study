# 문제 설명
# 1부터 N까지의 숫자 중 3, 6, 9가 들어가는 숫자는 - 표시를, 들어가지 않는 숫자는 해당 숫자를 출력한다.
# 3, 6, 9가 여러 번 들어가는 숫자의 경우, 3, 6, 9가 들어가는 숫자만큼 -를 출력한다.
# ex) 3는 -, 36은 --, 12는 12의 형태로 값을 출력한다.

T = int(input())
answer = ''
for test_case in range(1, T + 1):
    now = test_case
    yes = 0			# 각 자리수가 3, 6, 9 숫자인 경우를 개수를 셈
    no = 0			# 각 자리수가 3, 6, 9를 제외한 숫자인 경우를 셈
    while test_case >= 1:		# test_case / 10의 결과가 소수로 나타날 때 종료
        x = test_case % 10		# test_case 값의 마지막 자리 값을 파악하기
        if x == 3 or x == 6 or x == 9:
            yes += 1
        else:
            no += 1
        test_case = test_case // 10		# 몫 연산을 통해 다음 연산할 숫자를 갱신함
        
    if yes == 0:		# 3, 6, 9가 한번도 들어가지 않은 숫자인 경우
        answer += str(now)
    else:				# 3, 6, 9가 들어간 숫자인 경우 개수만큼 -를 더함
        answer += str("-"*yes)
    answer += " "
    
print(answer) 