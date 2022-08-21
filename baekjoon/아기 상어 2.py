"""
https://www.acmicpc.net/problem/17086
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()
ans = 0
arr = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 1:
            visited[i][j] = True
            q.append((i, j, 0))

dir = [(1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (1, -1), (-1, -1), (-1, 1)]
while q:
    x, y, num = q.popleft()
    ans = max(ans, num)
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        q.append((nx, ny, num+1))

print(ans)
