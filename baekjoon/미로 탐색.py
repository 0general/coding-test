'''
https://www.acmicpc.net/problem/2178
'''
from collections import deque

n, m = map(int, input().split())

road = [list(map(int, list(input()))) for _ in range(n)]
visit = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0

d = deque()

d.append([x, y])
while d:
    x, y = d.popleft()
    visit[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if road[nx][ny] == 1 and not visit[nx][ny]:
                road[nx][ny] += road[x][y]
                d.append([nx, ny])
            elif road[nx][ny] >= 1 and visit[nx][ny]:
                if road[nx][ny] > road[x][y] + 1:
                    road[nx][ny] == road[x][y] + 1

print(road[n-1][m-1])
