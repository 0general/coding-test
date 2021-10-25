"""
https://www.acmicpc.net/problem/13549
"""
from collections import deque

# 수빈이 위치 n, 동생 k
MAX = 200001
n, k = map(int, input().split())
time = 0
visited = [False]*MAX
q = deque()
ans = 0

visited[n] = True
q.append((n, time))
while q:
    now, t = q.popleft()
    if now == k:
        print(t)
        break
    x = 2*now
    for x in (now*2, now-1, now+1):
        if 0 <= x < MAX and not visited[x]:
            visited[x] = True
            if x == now*2:
                q.append((x, t))
            else:
                q.append((x, t+1))
