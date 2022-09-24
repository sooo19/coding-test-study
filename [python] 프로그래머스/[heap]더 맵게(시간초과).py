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