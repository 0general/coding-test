"""
https://www.acmicpc.net/problem/14567
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
pre = [0 for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    pre[b] += 1
    arr[a].append(b)

for i in range(1, N+1):
    if pre[i] == 0:
        visited[i] = 1
        q.append(i)

while q:
    x = q.popleft()
    for i in arr[x]:
        pre[i] -= 1
        if pre[i] == 0:
            visited[i] = visited[x] + 1
            q.append(i)

print(*visited[1:])
