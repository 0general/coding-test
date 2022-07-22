"""
https://www.acmicpc.net/problem/4179
"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

time = -1
fire = deque()
jihun = deque()

for i in range(r):
    for j in range(c):
        if arr[i][j] == "J":
            visited[i][j] = 1
            jihun.append((i, j, 0))
        elif arr[i][j] == "F":
            visited[i][j] = 2
            fire.append((i, j))

while time < 0 and (len(fire) or len(jihun)):
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + d[0], y + d[1]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or arr[nx][ny] == "#" or visited[nx][ny] == 2:
                continue
            visited[nx][ny] = 2
            fire.append((nx, ny))

    for _ in range(len(jihun)):
        x, y, t = jihun.popleft()
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + d[0], y + d[1]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                time = t+1
                break
            if arr[nx][ny] == "#" or visited[nx][ny] >= 1:
                continue
            visited[nx][ny] = 1
            jihun.append((nx, ny, t+1))
        else:
            continue
        break
    if time > 0:
        break

if time > 0:
    print(time)
else:
    print("IMPOSSIBLE")
