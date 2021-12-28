"""
https://www.acmicpc.net/problem/15686
BFS로 구현
"""
import sys
from collections import deque
from itertools import combinations as cm

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
chick = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2:
            chick.append((i, j))

answer = 2501
for c in cm(chick, m):  # 치킨집은 최대로 있어야 최단거리에 유리
    dist = 0
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    for sx, sy in c:
        visited[sx][sy] = 0
        q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if arr[nx][ny] == 1:
                    dist += visited[nx][ny]
                q.append((nx, ny))
    answer = min(answer, dist)

print(answer)
