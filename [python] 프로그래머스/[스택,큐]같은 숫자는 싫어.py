def solution(arr):
    answer = []
    answer.append(arr[0])       # 첫 번째 값 삽입

    for i in arr:       # answer 배열의 마지막 값이 현재 arr 요소와 같으면 skip, 다르면 answer 배열에 삽입
        if i != answer[-1]:
            answer.append(i)

    return answer