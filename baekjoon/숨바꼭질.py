"""
https://www.acmicpc.net/problem/1697
"""
from collections import deque

# 수빈이와 동생의 위치
n, k = map(int, input().split())
location = [0]*100001
q = deque()
cnt = 0
if n != k:
    q.append((n, cnt))
while q:
    now, cnt = q.popleft()
    if now == k:
        break
    for x in (now-1, now+1, now*2):
        if 0 <= x <= 100000 and location[x] == 0:
            location[x] = cnt+1
            q.append((x, cnt+1))

print(location[k])
