# 성적이 낮은 순서로 학생 이름 출력하기

# N 값 (학생 수) 입력 받기
n = int(input())

# (이름, 성적) 값 입력 받아 배열에 저장
result = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    result.append((name, score))

# 성적을 기준으로 정렬하기 위해 sorted 함수의 key 값에 넣을 함수 생상
def setting(data):
    return data[1]

# 정렬 (setting 함수를 Key 값으로 줌)
result = sorted(result, key=setting)        # lambda를 사용하지 않고 정렬한 경우
# result = sorted(result, key = lambda data:data[1])    # lambda를 사용해서 정렬한 경우

# 출력
for i in range(n):
    print(result[i][0], end = ' ')


