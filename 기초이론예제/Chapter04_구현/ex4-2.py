# 시각 => 구현(완전 탐색)

n = int(input())
count = 0   # 3이 들어가는 시각 개수 세기

for i in range(n+1):    # 시간
    for j in range(60):     # 분
        for k in range(60):     # 초
            if '3' in str(i)+str(j)+str(k):  # 문자열 합치기, 문자열 검사
                count+=1

print(count)
    