"""
https://www.acmicpc.net/problem/14940
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:  # 목표지점 2는 한 개 보장.
            visited[i][j] = 0
            q.append((i, j))
        elif arr[i][j] == 0:  # 원래 갈 수 없는 위치는 0으로 표시
            visited[i][j] = 0

while q:
    x, y = q.popleft()
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + d[0], y + d[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] >= 0:
            continue
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))

for i in range(n):
    print(*visited[i])
