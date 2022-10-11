# 시간 초과
# https://lute3r.tistory.com/m/240
# 위 블로그 참고해서 다시 코드 구현해보기

N = int(input())

input_list = []
for i in range(N):
    n = int(input())
    input_list.append(n)

input_list.sort()

for i in input_list:
    print(i)
