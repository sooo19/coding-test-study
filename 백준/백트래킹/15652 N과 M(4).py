# N과 M(4)
# 1부터 N까지의 숫자 중 중복하여 숫자를 골라 길이 M인 오름차순 수열을 만들어 출력하라.

N, M = map(int, input().split())
answer = []

def back(start):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(start, N+1):
        answer.append(i)
        back(i)
        answer.pop()

back(1)