n = int(input())    # 데이터 개수 입력 (줄바꿈)
data = list(map(int, input().split()))  # 공백을 기준으로 나눔

data.sort(reverse=True) # 내림차순
print(data)
