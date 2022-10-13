"""
https://www.acmicpc.net/problem/14923
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
hx -= 1
hy -= 1
ex -= 1
ey -= 1

ans = -1
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
if arr[hx][hy]:
    visited[hx][hy][1] = True
    q.append((0, hx, hy, 1))
else:
    visited[hx][hy][0] = True
    q.append((0, hx, hy, 0))

while q:
    dist, x, y, k = q.popleft()
    if x == ex and y == ey:
        ans = dist
        break
    for d in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nx, ny = x + d[0], y + d[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if arr[nx][ny] == 1 and k == 0 and not visited[nx][ny][1]:
            visited[nx][ny][1] = True
            q.append((dist+1, nx, ny, 1))
            continue
        if arr[nx][ny] == 0 and not visited[nx][ny][k]:
            visited[nx][ny][k] = True
            q.append((dist+1, nx, ny, k))

print(ans)
