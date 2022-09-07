# 삽입 정렬 (Insertion sort)
# 원리 : 처음에 맨 앞의 값은 정렬되었다고 가정하고, 남은 값들을 정렬된 부분과 비교해 올바른 위치에 삽입함

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # i부터 0까지 1씩 감소하면서 반복
        if array[j] < array[j-1]:   # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j] # 자기보다 큰 데이터를 만날때마다 계속 위치를 바꿈
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)