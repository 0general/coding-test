"""
https://www.acmicpc.net/problem/1600
"""
import sys
from collections import deque

input = sys.stdin.readline

hdir = [(2, 1), (2, -1), (1, -2), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
visited = [[[False for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
q = deque()

ans = -1

visited[0][0][0] = True
q.append((0, 0, 0, 0))

while q:
    x, y, total, num = q.popleft()
    if x == h-1 and y == w-1:
        ans = total
        break
    if num < k:
        for d in hdir:
            nx, ny = x+d[0], y+d[1]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny][num+1] or arr[nx][ny]:
                continue
            visited[nx][ny][num+1] = True
            q.append((nx, ny, total+1, num+1))
    for d in dir:
        nx, ny = x+d[0], y+d[1]
        if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny][num] or arr[nx][ny]:
            continue
        visited[nx][ny][num] = True
        q.append((nx, ny, total+1, num))

print(ans)
