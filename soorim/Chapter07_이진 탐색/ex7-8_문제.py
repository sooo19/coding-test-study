# 떡볶이 떡 만들기

# 떡의 개수, 요청한 떡의 길이 입력 받음
n, m = map(int, input().split())
arr_length = list(map(int, input().split()))

max_length = max(arr_length)
cut_length = [0]*max_length

def binary_search(cut_length, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # print('mid(절단기 길이): ', mid)

        for i in arr_length:
            if i-mid > 0:
                cut_length[mid] += i-mid
        
        # print(cut_length)   # 자른 떡의 길이의 합을 저장한 배열

        if cut_length[mid] == target:
            return mid
        elif cut_length[mid] < target:  # 타깃 값이 더 크면(떡을 더 길게 잘라야 하면) mid 값을 낮춰야 함
            end = mid - 1
        else:       # 타깃 값이 더 작으면(떡을 더 짧게 잘라야 하면) mid 값을 높여야 함
            start = mid + 1

    if start > end:
        return None

height = binary_search(cut_length, m, 0, max_length)  # m: target

if height == None:
    print('정답 없음')
else:
    print(height)