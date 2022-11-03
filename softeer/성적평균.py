import sys

N, K = map(int, input().split())        # N(학생 수), K(구간 수) 값 입력
score = input().split(" ")              # 점수 입력

for i in range(K):
    a, b = map(int, input().split())    # 구간 입력
    avg = 0
    for j in range(a-1, b):             # 구간에 따른 평균 값 계산
        avg += int(score[j])
    avg /= (b-a+1)                      # 전체 점수의 합 / 인원 수
    avg = round(avg, 2)                 # 소수점 2자리까지 반올림하여 구함
    print(format(avg, ".2f"))           # 소수점 2자리까지 출력 (계산 결과가 정수 또는 소수점 첫째자리에서 나눠떨어지는 경우 둘째자리까지 0으로 채워 출력)
