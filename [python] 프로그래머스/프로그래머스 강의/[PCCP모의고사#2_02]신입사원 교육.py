import heapq
def solution(ability, number):    
    queue = []
    for a in ability:
        heapq.heappush(queue, a)
    
    for _ in range(number):
        x = heapq.heappop(queue)
        y = heapq.heappop(queue)
        new = x + y
        heapq.heappush(queue, new)
        heapq.heappush(queue, new)
    
    return sum(queue)