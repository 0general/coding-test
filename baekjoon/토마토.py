"""
https://www.acmicpc.net/problem/7576
"""
import sys
from collections import deque


def bfs():
    result = 0
    while q:
        day, x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = 1
                q.append((day+1, nx, ny))
                result = day + 1
    return result


input = sys.stdin.readline
# n행 m열
m, n = map(int, input().split())
tomatoes = []
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 날짜

for i in range(n):
    tomatoes.append(list(map(int, input().split())))
    for j in range(m):
        if tomatoes[i][j] == 1:
            # 이미 익어있는 토마토 구함
            q.append((0, i, j))

result = bfs()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            result = -1
            break
    if result == -1:
        break

print(result)
