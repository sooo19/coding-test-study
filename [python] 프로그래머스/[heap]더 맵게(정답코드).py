import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)     # heap 배열을 생성해서 heapq를 사용해 배열 속에 스코빌배열 안의 요소들을 모두 집어넣는다. (자동으로 오름차순으로 저장된다)
    
    count = 0
    while heap[0] < K and len(heap) > 1:      # heap[0]값 (=최솟값)이 K보다 작은 동안, heap 배열의 요소 개수가 1개 이상인 경우만 실행
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        val = min1+min2*2
        heapq.heappush(heap, val)
        count += 1
    
    if heap[0] > K:
        return count
    else:
        return -1
        