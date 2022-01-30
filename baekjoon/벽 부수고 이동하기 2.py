"""
https://www.acmicpc.net/problem/14442
"""
from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
dist = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]
q = deque()

dist[0][0][0] = 1
q.append((0, 0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
out = 0

while q:
    x, y, num = q.popleft()
    if x == n-1 and y == m-1:
        out = dist[x][y][num]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == '0' and dist[nx][ny][num] == -1:
            dist[nx][ny][num] = dist[x][y][num]+1
            if nx == n-1 and ny == m-1:
                out = dist[x][y][num]+1
                break
            q.append((nx, ny, num))
        elif arr[nx][ny] == '1' and num < k and dist[nx][ny][num+1] == -1:
            dist[nx][ny][num+1] = dist[x][y][num]+1
            if nx == n-1 and ny == m-1:
                out = dist[x][y][num]+1
                break
            q.append((nx, ny, num+1))
    if out != 0:
        break


if out == 0:
    print(-1)
else:
    print(out)
