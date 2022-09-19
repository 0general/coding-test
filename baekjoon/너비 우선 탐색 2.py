"""
https://www.acmicpc.net/problem/24445
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
idx = 1
visited[R] = idx

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

q = deque()
q.append(R)

while q:
    now = q.popleft()
    edges[now].sort(reverse=True)
    for i in edges[now]:
        if not visited[i]:
            idx += 1
            visited[i] = idx
            q.append(i)

for i in range(1, N+1):
    print(visited[i])
