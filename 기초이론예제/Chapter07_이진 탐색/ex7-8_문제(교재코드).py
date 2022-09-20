# 떡볶이 떡 만들기

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2

    for i in array:
        if i > mid: # 자를 떡의 길이가 자를 길이보다 큰 경우만 연산 진행 (떡 길이가 음수가 나오면 안되기 때문)
            total += i-mid
    
    if total < m:       # 떡의 양이 부족한 경우
        end = mid-1
    else:
        result = mid    # 최대한 덜 잘랐을 때가 정답이기 때문에, 이때 result를 갱신
        start = mid+1
    

    # 내 코드

    # if total == m:
    #     result = mid
    #     print('result: ', result)
    #     break
    # elif total > m:     # 자른 떡의 길이가 목표보다 더 큼 (절단기 길이를 더 늘려야 함)
    #     start = mid+1
    #     print('start: ', start)
    # else:               # 자른 떡의 길이가 목표보다 더 작음 (절단기 길이를 더 줄여야 함)
    #     end = mid-1
    #     print('end: ', end)


print(result)
