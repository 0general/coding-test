"""
https://www.acmicpc.net/problem/1926
"""
from collections import deque
import sys


def bfs(i, j):
    q = deque()
    size = 0
    visited[i][j] = True
    q.append((i, j))
    while q:
        x, y = q.popleft()
        size += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and paper[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return size


input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
paper = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
num = 0
mx = 0

for i in range(N):
    for j in range(M):
        if paper[i][j] == 1 and not visited[i][j]:
            num += 1
            mx = max(mx, bfs(i, j))

print(num)
print(mx)
