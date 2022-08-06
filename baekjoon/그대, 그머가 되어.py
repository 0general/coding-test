"""
https://www.acmicpc.net/problem/14496
"""
import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
q = deque()
visited[a] = True
q.append((a, 0))
ans = -1
arr = [[] for _ in range(n+1)]
for _ in range(m):
    c, d = map(int, input().split())
    arr[c].append(d)
    arr[d].append(c)

while q:
    now, dist = q.popleft()
    if now == b:
        ans = dist
        break
    for i in arr[now]:
        if not visited[i]:
            visited[i] = True
            q.append((i, dist+1))

print(ans)
