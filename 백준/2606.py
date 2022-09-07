# 웜 바이러스 (백준 2606번)
# BFS
# 각 컴퓨터는 연결된 네트워크가 있으며 연결되어 있는 컴퓨터는 웜 바이러스가 전염됨
# 주어진 웜 바이러스 컴퓨터에 의해 바이러스에 감염되는 컴퓨터들의 개수 구하기

from collections import deque

n = int(input())    # 컴퓨터의 수
m = int(input())    # 네트워크 상 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]   # graph 배열 만들어서 연결된 노드 정보를 저장

for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)      # 양방향이므로 모두 저장
    graph[b].append(a)

visited = [0]*(n+1)      # 방문 여부 저장

queue = deque([1])  # 1번 컴퓨터가 웜 바이러스에 걸림
visited[1] == 1
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1

count = 0   # 감염된 컴퓨터의 수
for i in range(2, n+1):
    if visited[i] == 1:
        count += 1

print(count)
