# 계수 정렬

# 원리 
# : 정렬할 배열에 등장하는 숫자의 개수만큼 index를 가지는 배열을 만든다.
# : 각 index에 해당하는 숫자가 등장하는 수를 counting해서 배열 값으로 가진다.
# : counting을 마치고 배열을 완성한 후 해당 인덱스를 배열 값 만큼 출력한다.

# 선택 정렬, 삽입 정렬, 퀵 정렬은 데이터를 비교하여 위치를 변경하는 '비교 기반의 정렬 알고리즘'이다.
# 계수 정렬은 이에 해당하지 않는다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# counting할 배열 생성
count = [0]*(max(array)+1)

# 각 데이터에 해당하는 인덱스의 값 증가
for i in array:
    count[i] = count[i]+1

# 결과 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')