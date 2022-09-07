# 모험가 길드

n = int(input())
X = list(map(int, input().split()))

X.sort()

count = 0   # 한 팀의 인원 수
result = 0  # 팀 개수
for i in X:
    # 인원 수가 i인 팀
    count += 1      # 현재 그룹에 해당 모험가를 포함시킴

    if count >= i:      # count >= i인 이유는 i가 다음으로 넘어가면 항상 더 큰 값이므로 넘어간 i 만큼의 인원이 팀에 포함되어야 함
        result += 1
        count = 0

print(result)