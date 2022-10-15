# 우선순위 큐는 데이터를 추가한 순서대로 제거하는 선입선출 (FIFO)의 특성을 가진 일반적인 큐의 자료구조와 달리
# 데이터 추가는 어떤 순서대로 해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 독특한 특성을 지닌 자료구조이다.
# 내부적으로 데이터를 정렬된 상태로 보관하는 메커니즘이 있다 (heapq 모듈을 통해 구현되어 있다.)

from queue import PriorityQueue

que = PriorityQueue()       # 우선순위 큐 초기화
que = PriorityQueue(maxsize = 8)        # 우선순위 큐의 디폴트 사이즈는 무한대이므로, 특정 최대 크기가 필요하다면 설정

# 우선순위 큐에 원소 추가 (put)
que.put(4)
que.put(1)
que.put(7)
que.put(3)

# 우선순위 큐에 원소 삭제 (get)
# 값의 크기 순서대로 1, 3, 4, 7순으로 삭제됨
print(que.get())
print(que.get())
print(que.get())
print(que.get())

# 정렬 기준 변경
# 단순 오름차순이 아닌 다른 기준으로 원소를 정렬하고 싶다면, 
# (우선순위, 값)의 튜플의 형태로 데이터를 추가 및 제거하면 된다.
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

print(que.get()[1])     # 값을 하나씩 제거할 때마다 다른 값들의 우선순위가 1씩 줄어들면서 변경됨
print(que.get()[1])
print(que.get()[1])