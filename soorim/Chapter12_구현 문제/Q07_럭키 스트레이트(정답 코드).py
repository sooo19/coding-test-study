# 럭키 스트레이트 (정답 코드)
# 배열 사용 X

n = input()

left, right = 0, 0
for i in range(int(len(n)/2)):
    left += int(n[i])
    right += int(n[int(len(n))-i-1])

if left == right:
    print('LUCKY')
else:
    print('READY')
