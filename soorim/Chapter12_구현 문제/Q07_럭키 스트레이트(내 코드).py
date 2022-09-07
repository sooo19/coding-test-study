# 럭키 스트레이트 (내 코드)
# 입력 예시 : 123402

# 점수 N 입력 받음
N = int(input())    # 입력 받은 숫자를 정수형으로 변환함

# 배열에 점수의 각 자리수를 저장 (나누기 연산과 몫 계산 연산 활용)
arr = []
while N >= 1:
    arr.append(N%10)
    N//=10

# 왼쪽, 오른쪽 점수의 합을 각각 구함 (배열에는 가장 오른쪽 자리수의 점수부터 첫 인덱스에 저장됨)
# ex) 123402 => [2, 0, 4, 3, 2, 1] 로 저장됨
right, left = 0, 0
for i in range(int(len(arr)/2)):
    right += arr[i]
    left += arr[len(arr)-i-1]

# 점수가 같으면 LUCKY, 다르면 READY 출력
if right == left:
    print('LUCKY')
else:
    print('READY')
