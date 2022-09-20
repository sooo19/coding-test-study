# 주사위 2개 던지기 (주사위 눈 출력)
a, b = map(int, input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)