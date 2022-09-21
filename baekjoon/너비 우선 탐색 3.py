"""
https://www.acmicpc.net/problem/24446
"""
import sys
from collections import deque

N, M, R = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

visited[R] = 0
q = deque()
q.append(R)

while q:
    now = q.popleft()
    for x in edges[now]:
        if visited[x] == -1:
            visited[x] = visited[now] + 1
            q.append(x)

for i in range(1, N+1):
    print(visited[i])
