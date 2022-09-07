# queue

from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.popleft()
queue.append(1)

# queue.reverse()

print(queue)