# N과 M (3)
# 수열을 구할 때, 같은 수를 여러 번 골라도 된다.

N, M = map(int, input().split())
answer = []

def back():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return              # 리턴 값이 없더라도, 함수에서 return문이 없으면 오류 발생하므로 꼭 있어야 한다

    for i in range(1, N+1):
        answer.append(i)
        back()
        answer.pop()

back()