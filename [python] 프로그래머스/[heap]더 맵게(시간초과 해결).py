# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 함수를 구현해라.

# 아래 코드는 시간 초과되는 코드이다.

import heapq

def solution(scoville, K):
    answer = 0
    
    while(1):  
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        
        if min1 < K:
            new = min1 + min2*2
            heapq.heappush(scoville, new)
            answer += 1
        else:
            return answer


# 위 코드의 시간 초과 문제를 해결
# import heapq

# def solution(scoville, K):
#     heap = []
#     for i in scoville:
#         heapq.heappush(heap, i)     # heap 배열을 생성해서 heapq를 사용해 배열 속에 스코빌배열 안의 요소들을 모두 집어넣는다. (자동으로 오름차순으로 저장된다)
    
#     count = 0
#     while(1):      # heap[0]값 (=최솟값)이 K보다 작은 동안, heap 배열의 요소 개수가 1개 이상인 경우만 실행
#         min1 = heapq.heappop(heap)
#         min2 = heapq.heappop(heap)
#         val = min1+min2*2
#         heapq.heappush(heap, val)
#         count += 1
        
#         if len(heap) == 1 or heap[0] > K:     # => 여기서 시간 초과 발생
#             break
    
#     if heap[0] > K:
#         return count
#     else:
#         return -1
        
# heap[0]과 heapq.heappop(heap) 모두 heap 배열에서 가장 작은 요소를 가리키는 방법이다
# 하지만 heapq.heappop(heap) 연산은 heap[0]을 통해 값을 지칭하는 것보다 오랜 시간이 소요된다. (값을 빼줘야하기 때문에 단순히 값을 지칭하는 것과는 시간 차이가 존재)
# 따라서 값의 대소 비교만 하는 경우에는 pop을 해주지 않고 해당 요소를 가리켜 값을 확인해야 한다.