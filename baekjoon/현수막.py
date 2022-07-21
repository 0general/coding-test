"""
https://www.acmicpc.net/problem/14716
"""
import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

q = deque()
ans = 0

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        if arr[i][j] == 1:
            visited[i][j] = True
            ans += 1
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= M or ny >= N or visited[nx][ny] or arr[nx][ny] == 0:
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny))

print(ans)
