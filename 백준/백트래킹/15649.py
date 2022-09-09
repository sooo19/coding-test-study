# 15649번 : N과 M (1)

# 방법 1) 백트래킹 사용

# N : 1부터 N까지의 숫자를
# M : 조합해서 길이가 M인 숫자를 만들어라

N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:
        # 숫자 배열 print
        print(" ".join(map(str, ans)))
        return      # ans 값을 출력하면 return (다시 새로운 배열 생성)
    
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            back()      # 재귀 (계속 뒤에 새 숫자 가져옴)
            ans.pop()       # 가장 마지막에 들어온 숫자를 뺌 (전 단계로 돌아감)

back()

# 파이썬 join 함수
# ''.join(리스트) : 매개변수로 들어온 ['a', 'b', 'c'] 와 같은 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수


# 방법 2)
# itertools 라이브러리 사용

from itertools import permutations

N, M = map(int, input().split())
ans = permutations(range(1, N+1), M)

for i in ans:
    print(" ".join(map(str, i)))
