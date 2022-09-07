# 선택 정렬 (Selection sort)
# 원리 : 처음에 맨 앞의 값이 최솟값이라고 가정하고, 계속해서 남은 숫자 중 가장 작은 숫자를 골라 swap해줌

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    # array[min_index]는 새로운 최솟값, array[i]는 앞에서부터 한 자리씩 뒤로 옮겨가며 만나는 값

print(array)