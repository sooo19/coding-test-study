# N과 M(2)

N, M = map(int, input().split())
ans = []

def back(start):
    # 출력
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    # 숫자 배열 생성
    for i in range(start, N+1):     # 앞에서 사용한 숫자보다 큰 숫자만 사용해야 함
        if i not in ans:
            ans.append(i)       # i를 숫자 배열에 입력
            back(i+1)              # 앞서 입력한 i보다 큰 숫자만 가지고 숫자 배열을 완성해야 함
            ans.pop()

start = 1
back(start)